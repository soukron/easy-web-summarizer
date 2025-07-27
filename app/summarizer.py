import argparse

from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama
from langchain_community.document_loaders import WebBaseLoader


def setup_argparse():
    """Setup argparse to parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Summarize a document from a given URL and optionally translate it."
    )
    parser.add_argument(
        "-u", "--url", required=True, help="URL of the document to summarize"
    )
    parser.add_argument(
        "-t", "--translate", 
        help="Target language for translation (if specified, translation is enabled)"
    )
    return parser.parse_args()


def load_document(url):
    """Load document from the specified URL."""
    loader = WebBaseLoader(url)
    return loader.load()


def setup_summarization_chain():
    """Setup the summarization chain with a prompt template and ChatOllama."""
    prompt_template = PromptTemplate(
        template="""As a professional summarizer, create a detailed and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines:
            1. Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity.

            2. Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.

            3. Rely strictly on the provided text, without including external information.

            4. Format the summary in paragraph form for easy understanding.

            5.Conclude your notes with [End of Notes, Message #X] to indicate completion, where "X" represents the total number of messages that I have sent. In other words, include a message counter where you start with #1 and add 1 to the message counter every time I send a message.

        By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, detailed, and reader-friendly manner. Optimize output as markdown file.

        "{text}"

        DETAILED SUMMARY:""",
        input_variables=["text"],
    )

    llm = ChatOllama(model="llama3:instruct", base_url="http://127.0.0.1:11434")
    llm_chain = LLMChain(llm=llm, prompt=prompt_template)
    return llm_chain


def setup_translation_chain(target_language="Turkish"):
    """Setup the translation chain with a prompt template and ChatOllama."""
    prompt_template = PromptTemplate(
        template="""Translate the following text into {target_language}. Provide only the translation without any quotes, headers, or additional text. The output should be clean and direct:

{text}

TRANSLATION:""",
        input_variables=["text", "target_language"],
    )

    llm = ChatOllama(model="llama3:instruct", base_url="http://127.0.0.1:11434")
    llm_chain = LLMChain(llm=llm, prompt=prompt_template)
    return llm_chain


def translate_text(text, target_language="Spanish"):
    """Translate text to the specified target language."""
    llm_chain = setup_translation_chain(target_language)
    result = llm_chain.run({"text": text, "target_language": target_language})
    return result


def main():
    args = setup_argparse()
    docs = load_document(args.url)

    # Generate summary
    llm_chain = setup_summarization_chain()
    summary = llm_chain.run(docs)
    
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(summary)
    print()
    
    # Translate if language is specified
    if args.translate:
        print("=" * 60)
        print(f"TRANSLATION TO {args.translate.upper()}")
        print("=" * 60)
        try:
            translation = translate_text(summary, args.translate)
            print(translation)
        except Exception as e:
            print(f"Translation failed: {e}")
            print("Make sure Ollama is running with the llama3:instruct model.")


if __name__ == "__main__":
    main()

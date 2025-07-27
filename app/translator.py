from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama


def setup_translator_chain(target_language="Turkish"):
    """Setup the translation chain with a prompt template and ChatOllama."""
    prompt_template = PromptTemplate(
        template="""As a professional translator, provide a detailed and comprehensive translation of the provided text into {target_language}, ensuring that the translation is accurate, coherent, and faithful to the original text.

        "{text}"

        DETAILED TRANSLATION:""",
        input_variables=["text", "target_language"],
    )

    llm = ChatOllama(model="llama3:instruct", base_url="http://127.0.0.1:11434")
    llm_chain = LLMChain(llm=llm, prompt=prompt_template)
    return llm_chain


def translate_text(text, target_language="Turkish"):
    """Translate text to the specified target language."""
    llm_chain = setup_translator_chain(target_language)
    result = llm_chain.run({"text": text, "target_language": target_language})
    return result

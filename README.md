# Easy Webpage Summarizer

A Python script designed to summarize webpages from specified URLs using the LangChain framework and the ChatOllama model. It leverages advanced language models to generate detailed summaries and translate them to multiple languages, making it an invaluable tool for quickly understanding the content of web-based documents.

## Requirements

[ollama](https://ollama.com/) must be installed and served

```bash
ollama run llama3:instruct
```

```bash
pip install -r requirements.txt
```

## Features

- Summarization of webpages and youtube videos directly from URLs.
- **Translation to multiple languages** with language selection
- Integration with LangChain and ChatOllama for state-of-the-art summarization and translation.
- Command-line interface for easy use and integration into workflows.
- Web interface with language selection dropdown.

## Usage

### Command Line Interface

To use the webpage summarizer, run the script from the command line, providing the URL of the document you wish to summarize:

```bash
# Basic summarization only
python app/summarizer.py -u "http://example.com/document"

# Summarize and translate to Turkish (default)
python app/summarizer.py -u "http://example.com/document" -t "Turkish"

# Summarize and translate to French
python app/summarizer.py -u "http://example.com/document" -t "Spanish"

# Summarize and translate to German
python app/summarizer.py -u "http://example.com/document" -t "German"
```

Replace `http://example.com/document` with the actual URL of the document you want to summarize.

#### Available Languages

The following languages are supported for translation:
- Turkish (default)
- French
- German
- Italian
- Portuguese
- Spanish
- English

### Web UI

To use the webpage summarizer in your web browser, you can also try the gradio app:

```bash
python app/webui.py
```

![gradio](assets/gradio.png)

The web interface includes:
- URL input for summarization
- Language selection dropdown (appears after generating summary)
- Translate button to convert summary to selected language

## Docker

```bash
docker build -t web_summarizer .
docker run -p 7860:7860 web_summarizer

# Run if you run ollama on host
docker run -d --network='host' -p 7860:7860 web_summarizer
```

## Development

To contribute to the development of this script, clone the repository, make your changes, and submit a pull request. We welcome contributions that improve the script's functionality or extend its capabilities.

- [x] Summarize youtube videos
- [x] Dockerize project
- [x] Translate to different languages
- [x] Language selection for translations
- [ ] Streaming text output on gradio
- [ ] Serve on web

## License

This script is released under the MIT License. See the [LICENSE](./LICENSE) file in the repository for full details.

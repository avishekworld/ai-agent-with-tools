# AI Agent with Tools

This project is an AI-powered research assistant that leverages large language models (LLMs) and external tools to generate research papers, search the web, query Wikipedia, and save the research report to a file using agent tools. It uses [LangChain](https://github.com/langchain-ai/langchain), [Ollama](https://ollama.com/), and various community tools.

## Features

- **Web Search:** Uses DuckDuckGo to search the web for up-to-date information.
- **Wikipedia Query:** Retrieves concise information from Wikipedia.
- **Research Paper Generation:** Generates structured research outputs with title, summary, sources, and tools used.
- **Save to File:** Saves research outputs with timestamps to a local file.

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) running locally with the `llama3.2:3B` model
- See [requirements.txt](requirements.txt) for Python dependencies

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/ai-agent-with-tools.git
    cd ai-agent-with-tools
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up your `.env` file if needed (for environment variables).

## Usage

Run the main application:

```sh
python app.py
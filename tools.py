from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="DuckDuckGoSearch",
    func=search.run,
    description="Search the web for information.",
)

wiki_api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

def save_file(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, 'a', encoding="utf-8") as file:
        file.write(formatted_text)
    
    return f"Research paper successfully saved to {filename}"

save_file_tool = Tool(
    name="SaveFile",
    func=save_file,
    description="Saves the content to a file with the current timestamp in the filename",
)
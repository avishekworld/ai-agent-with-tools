from langchain_community.chat_models import ChatOllama
#from langchain.llms import Ollama
#from langchain.chat_models import ChatOllama
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
#from langchain_core.output_parsers import PydanticOutputParser
from langchain.output_parsers import PydanticOutputParser
from dotenv import load_dotenv
from tools import search_tool, wiki_tool, save_file_tool

load_dotenv()

class ResearchResponse(BaseModel):
    title: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatOllama(model="llama3.2:3B")
#response = llm.invoke("What is Generative AI, AI Agent, LLM?")
#print(response)
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", 
         """You are a reasearch assistant that will help generate a research paper.
         Answer the user query and use necessary tools.
         Wrap the output in this format and provide no other text:{output_format}
         """),
        ("placeholder", "{chat_history}"), 
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(output_format=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_file_tool]

agent = create_tool_calling_agent(
    llm = llm,
    prompt = chat_template,
    tools = tools,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
    )

query = input("What research can I help you with: ")
# Top small businesses in Westcoast and save the output to a file
raw_response = agent_executor.invoke({       
    "query": query
})
print(raw_response)

try:
    output = raw_response.get("output")
    if output and isinstance(output, list) and len(output) > 0 and "text" in output[0]:
        structured_response = parser.parse(output[0]["text"])
        print(structured_response)
    else:
        print("Error: 'output' is missing or not in the expected format:", output)
except Exception as e:
    print(f"Error parsing response: {e}  Raw Response {raw_response}")

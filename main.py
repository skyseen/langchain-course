from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_tavily import TavilySearch

load_dotenv()

llm = ChatOpenAI()
tools = [TavilySearch()]
agent = create_agent(model=llm, tools=tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": [HumanMessage(content="search for the latest apple products news and summarise the details")]})
    print(result)

if __name__ == "__main__":
    main()

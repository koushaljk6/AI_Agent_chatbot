#Step 1: Set up API keys for Groq, OpenAI and Tavily
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

#Step 2: setup LLM and Tools
'''
run this command in cmd, after deactivating (deactivate) pipenv shell (pipenv environment)
pipenv install langchain_groq langchain_openai langchain_communit
'''
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

#we are using tavily so that othe llm can live search on internet, as we know LLm don;t have live access

search_tool=TavilySearchResults(max_results=2) #max-results will return the 2 searches(like on google when we search,
                                                #we get various URLs of different websites)

#Step 3: Setup AI Agent with search tool functionality

# to build agents we need langgraph-> pipenv install langgraph
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as an AI chatbot who is smart and friendly, having a mix of accuracy and creativity depends upon user's prompt."

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    try:
        if provider == "Groq":
            llm = ChatGroq(model=llm_id)
        elif provider == "OpenAI":
            llm = ChatOpenAI(model=llm_id)
        
        tools=[TavilySearchResults(max_results=2)] if allow_search else [] #max-results will return the 2 searches(like on google when we search,
                                                    #we get various URLs of different websites)
        agent=create_react_agent(
            model=llm,
            tools=tools,
            state_modifier=system_prompt
        )

        state = {"messages":query}
        response = agent.invoke(state)
        messages=response.get("messages")
        ai_messages=[message.content for message in messages if isinstance(message,AIMessage)]
        if ai_messages:
                return ai_messages[-1]
        else:
                return "Error: No messages returned by the AI agent"
    except Exception as e:
        return f"Error: {str(e)}"

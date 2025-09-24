import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_experimental.agents.agent_toolkits import create_python_agent


load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(model='gpt-4.1-nano')
wikipedia_tool = WikipediaQueryRun(
   api_wrapper=WikipediaAPIWrapper(
       lang='pt'
   )
)

agent_executor = create_python_agent(
   llm=model,
   tool=wikipedia_tool,
   verbose=True,
)

prompt_template = PromptTemplate(
   input_variables=['query'],
   template='''
   Searches the web for {query} and provides a summary of the topic.
   '''
)

query = input('What do you want to consult?\n==> ')
prompt = prompt_template.format(query=query)

response = agent_executor.invoke(prompt)
print(response.get('output'))

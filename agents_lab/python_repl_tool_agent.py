import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_experimental.utilities import PythonREPL
from langchain.agents import Tool
from langchain_experimental.agents.agent_toolkits import create_python_agent


load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
model = ChatOpenAI(model='gpt-4.1-nano')

python_repl = PythonREPL()
python_repl_tool = Tool(
   name='Python REPL',
   description = 'A Python shell. Use this to execute Python code. Execute only valid Python code.' +
                 'If you need to get the output of the code, use the "print(...)" function.',
   func=python_repl.run
)

agent_executor = create_python_agent(
   llm=model,
   tool=python_repl_tool,
   verbose=True,
)

prompt_template = PromptTemplate(
   input_variables=['query'],
   template='''
   Solve the problem: {query}.
   '''
)

query = r'What is 20% of 300?'
prompt = prompt_template.format(query=query)
response = agent_executor.invoke(prompt)

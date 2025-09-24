import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import Tool, create_react_agent, AgentExecutor
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.utilities import PythonREPL
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_python_agent


load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
model = ChatOpenAI(model='gpt-4.1-nano')

prompt = '''
As a personal financial assistant, you'll answer questions and provide financial and investment tips.
Answer all questions in Brazilian Portuguese.
Questions: {q}
'''
prompt_template = PromptTemplate.format_prompt(prompt)

python_repl = PythonREPL()
python_repl_tool = Tool(
    name ='Python REPL',
    description = 'A Python shell. Use this to run Python code. Run only valid Python code.' +
                  'If you need to get the output of the code, use the "print(...)" function.' +
                  'Use it to perform financial calculations needed to answer questions and provide tips.',
    func=python_repl.run
)

search = DuckDuckGoSearchRun()
duckduckgo_tool = Tool(
    name = 'DuckDuckGo Search',
    description = 'Useful for finding information and tips on saving and investing options.' +
                  'You should always search the internet for the best tips for this tool, not' +
                  'answer directly. Your answer should indicate that there are elements you researched on the internet.',
    func = search.run()
)

react_instructions = hub.pull('hwchase17/react', include_model=True)

tools = [python_repl_tool, duckduckgo_tool]

agent = create_react_agent(
    llm = model,
    tools = tools,
    prompt = react_instructions,
)

agent_executor = AgentExecutor(
    agent = agent,
    tools = tools,
    verbose = True,
)

question = '''
My income is R$10,000 per month, and I have several credit cards totaling R$12,000 per month.
I also have R$1,500 in rent and fuel expenses.
What tips can you give me?
'''


output = agent_executor.invoke(
    {'input': prompt_template.__format__(q=question)}
)

print(output.get('output'))
import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_openai import ChatOpenAI


load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
model = ChatOpenAI(model='gpt-4o-mini')

db = SQLDatabase.from_uri('sqlite:///data/ipca.db')

toolkit = SQLDatabaseToolkit(
    db=db,
    llm=model
)

system_message = hub.pull('hwchase17/react')

agent = create_react_agent(
    llm = model,
    tools = toolkit.get_tools(),
    prompt = system_message,
)

agent_executor = AgentExecutor(
    agent = agent,
    tools = toolkit.get_tools(),
    verbose = True,
)

prompt = '''
Use the necessary tools to answer questions related to the IPCA's history over the years.
Answer all questions in Brazilian Portuguese.
Questions: {q}
'''

prompt_template = PromptTemplate.from_template(prompt)
question = '''
Based on historical IPCA data since 2004,
predict the IPCA values ​​for each future month until the end of 2025.
'''

output = agent_executor.invoke({
    'input': prompt_template.format(q=question)
})

print(output.get('output'))

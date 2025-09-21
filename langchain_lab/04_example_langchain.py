import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')


model = ChatOpenAI(
   model='gpt-4.1-nano',
)


chat_template = ChatPromptTemplate.from_messages(
   [
       SystemMessage(content='You should answer based on geographic data from countries of South America.'),
       HumanMessagePromptTemplate.from_template('Please tell me about the country {country}.'),
       AIMessage(content='Of course, I will start by collecting information about the country and analyzing the available data.'),
       HumanMessage(content='Be sure to include demographic data.'),
       AIMessage(content='Got it! Here is the data:'),
   ]
)


prompt = chat_template.format_messages(country='Brazil')
response = model.invoke(prompt)
print(response.content)
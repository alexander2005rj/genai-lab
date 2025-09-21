import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
model = ChatOpenAI(
   model='gpt-4.1-nano',
)

classification_chain = (
   PromptTemplate.from_template(
       '''
       Classify the user's question into one of the following categories:
       - Financial
       - Technical Support
       - Other Information
       
       Question: {question}
       '''
   )
   | model
   | StrOutputParser()
)

financial_chain = (
    PromptTemplate.from_template(
       '''
       You are a financial expert.
       Always answer questions beginning with "Welcome to the Financial Sector."
       Answer the user's question:
       Question: {question}
       '''
   )
   | model
   | StrOutputParser()
)

tech_support_chain = (
    PromptTemplate.from_template(
       '''
       You are a technical support specialist.
       Always answer questions beginning with "Welcome to Technical Support."
       Answer the user's question:
       Question: {question}
       '''
   )
   | model
   | StrOutputParser()
)

other_support_chain = (
    PromptTemplate.from_template(
       '''
       You are a general information assistant.
       Always answer questions beginning with "Welcome to the general information section."
       Answer the user's question:
       Question: {question}
       '''
   )
   | model
   | StrOutputParser()
)

def route(classification):
   classification = classification.lower()
   if 'financial' in classification:
       return financial_chain
   elif 'technical support' in classification:
       return tech_support_chain
   else:
       return other_support_chain


question = input('What is your question?\n==> ')
classification = classification_chain.invoke(
   {'question': question}
)

response_chain = route(classification=classification)
response = response_chain.invoke(
   {'question': question}
)

print(response)
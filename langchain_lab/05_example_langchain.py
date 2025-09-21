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

runnable_sequence = (
   PromptTemplate.from_template(
       "Tell me about the car {car}."
   )
   | model
   | StrOutputParser()
)

response = runnable_sequence.invoke({'car': 'Mitsubishi GTO Twin Turbo'})
print(response)
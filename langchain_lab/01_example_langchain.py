from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')

model = ChatOpenAI(
   model = 'gpt-4.1-nano',
)

messages = [
   {'role': 'system', 'content': 'Você é um assistente de história mundial'},
   {'role': 'user', 'content': 'Quem foi Alan Turing?'}
]

response = model.invoke(messages)

print(response)
print(response.content)

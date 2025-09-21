from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv('API_KEY')
)

response = client.chat.completions.create(
    model='gpt-4.1-nano',
    messages=[
        {
            'role': 'system',
            'content': 'Provide technical answers about programming. Act like an experienced Python programmer, an expert in design patterns and clean architecture.'
        },
        {
            'role': 'user',
            'content': 'Tell me how I can create a restful API.'
        }
    ],
    temperature=0.8
)

print(response.choices[0].message.content)

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
model = ChatOpenAI(
   model='gpt-4.1-nano',
)

template = '''
Translate text from {language1} to {language2}: {text}
'''

prompt_template = PromptTemplate.from_template(
   template = template
)

prompt = prompt_template.format(
   language1 = 'english',
   language2 = 'french',
   text = "I'm excited to learn more and more about Langchain's features."
)

response = model.invoke(prompt)
print(response.content)

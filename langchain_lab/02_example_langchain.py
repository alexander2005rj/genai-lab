import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_community.cache import InMemoryCache, SQLiteCache
from langchain.globals import set_llm_cache


load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
model = OpenAI()

set_llm_cache(
    # InMemoryCache()
    SQLiteCache(database_path='openai_cache.db')
)

prompt = 'Tell me who Dennis Ritchie was.'

response1 = model.invoke(prompt)
print(f'My first call: {response1}')

response2 = model.invoke(prompt)
print(f'My second call: {response2}')

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader


load_dotenv()
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
model = ChatOpenAI(
   model='gpt-4.1-nano',
)

loader = TextLoader('examples_docs/renault_sandero.txt')
documents = loader.load()

loader = PyPDFLoader('examples_docs/renault_stepway.pdf')
documents = loader.load()

loader = CSVLoader('examples_docs/renault_models.csv')
documents = loader.load()

prompt_knowledge_base = PromptTemplate(
   input_variables=['context', 'question'],
   template='''
   Use the following context to answer the question.
   Answer only based on the information provided.
   Do not use information outside the context:
   Context: {context}
   Question: {question}'''
)

question = input('What is your question?\n==> ')
chain = prompt_knowledge_base | model | StrOutputParser()
response = chain.invoke(
   {
       'context': '\n'.join(doc.page_content for doc in documents),
       'question': question,
   }
)

print(response)
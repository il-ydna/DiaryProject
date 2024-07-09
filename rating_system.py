import os
import openai
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openaikey = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(api_key=openaikey)

llm.invoke('what are the colors of the rainbow')

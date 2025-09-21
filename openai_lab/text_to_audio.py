from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv('API_KEY')
)


response = client.audio.speech.create(
    model='tts-1',
    voice='echo',
    input='I am really enjoying learning about generative AI. I can imagine countless use cases in my day-to-day life.',
)

response.write_to_file('result_audio/test_audio.mp3')
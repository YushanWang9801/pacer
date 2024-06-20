from openai import OpenAI
from decouple import config

OPENAI_API_KEY = config('OPENAI_API_KEY')

client = OpenAI(
    base_url="https://api.gptsapi.net/v1",
    api_key= OPENAI_API_KEY
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)
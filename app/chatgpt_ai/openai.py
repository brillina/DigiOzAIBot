
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key = os.environ.get('CHATGPT_API_KEY')
)


def chatgpt_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=1,
        max_tokens=0
    )
    choices = response.choices
    if choices and len(choices) > 0:
        prompt_response = choices[0].message['content'].strip()
        return prompt_response
    return None
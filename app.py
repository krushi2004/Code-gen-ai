import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_code(prompt, language="Python"):
    full_prompt = f"Write a {language} function for the following request:\n{prompt}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "user",
            "content": full_prompt
        }]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    print("GenAI Code Generator")
    language = input("Enter the programming language (default: Python): ") or "Python"
    while True:
        prompt = input("Describe what you want the code to do (or type 'exit' to quit): ")
        if prompt.lower() in ['exit', 'quit']:
            break
        code = generate_code(prompt, language)
        print(f"\nGenerated {language} code:\n{code}\n")

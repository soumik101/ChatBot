import os
from openai import OpenAI

# Initialize client with API key (set it as an environment variable for safety)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",   # or "gpt-4" if you have access
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    print("Chatbot is ready! Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = chat_with_gpt(user_input)
        print("Chatbot:", response)

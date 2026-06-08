from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = "You are a helpful assistant. Be concise - max 3 sentences per reply."

messages = []

print("Chatbot ready. Type /clear to reset, /quit to exit.\n")

while True:
    user_input = input("You: ").strip()

    if not user_input:
        continue

    if user_input == "/quit":
        print("Bye!")
        break

    if user_input == "/clear":
        messages = []
        print("Memory cleared.\n")
        continue

    # This is the INDUSTRY STANDARD format - same as OpenAI
    # role: "user" or "assistant" (not "model" like Gemini)
    # content: plain string (not "parts" like Gemini)
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages
)
    

    reply = response.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})

    print(f"AI: {reply}")
    print(f"    [{len(messages)} messages in memory]\n")
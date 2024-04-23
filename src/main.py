from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


from listener import listen
from speaker import speak
from chatgpt import get_response

def main():
    while True:
        text = listen()
        if text:
            response = get_response(text, api_key)
            speak(response)

if __name__ == "__main__":
    main()

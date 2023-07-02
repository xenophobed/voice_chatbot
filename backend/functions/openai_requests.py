import openai
import os
from decouple import config

from functions.database import get_recent_messages

# Retrieve Enviornment Variables
openai.api_key = config("OPENAI_API_KEY")


# os.environ['OPENAI_API_BASE'] = "https://api.ai-yyds.com/v1"
# os.environ['OPENAI_API_KEY'] = "sk-gt4GSEcL4ZGkmlCy3d12BcAb348e4dE983D63f8f619aFc76"


# Open AI - Whisper
# Convert audio to text
def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        return


# Open AI - Chat GPT
# Get response to our message
def get_chat_response(message_input):
    messages = get_recent_messages()
    user_message = {"role": "user",
                    "content": message_input + "keep it simple and ask me for more information if you don't know the answer"}
    messages.append(user_message)
    print(messages)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        message_text = response["choices"][0]["message"]["content"]
        return message_text
    except Exception as e:
        return

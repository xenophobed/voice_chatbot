import openai
from decouple import config

from functions.database import get_recent_messages

# Retrieve Enviornment Variables
openai.api_key = config("OPENAI_API_KEY")


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

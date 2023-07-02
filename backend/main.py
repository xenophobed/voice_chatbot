# uvicorn main:app
# uvicorn main:app --reload

# Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Customer Function Imports
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages

# Initiate App
app = FastAPI()

# CORS -Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4173",
    "http://localhost:3000",
]

# CORS -Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Check Health
@app.get("/health")
async def check_health():
    return {"message": "Healthy"}


# Reset Messages
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "conversation reset"}


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Get audio
@app.get("/post-audio-get/")
async def get_audio():
    audio_input = open("voice.mp3", "rb")

    # Decode Audio
    message_decoded = convert_audio_to_text(audio_input)

    # Guard: ensure message decoded
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode Audio")

    # Get chatGPT response
    chat_response = get_chat_response(message_decoded)

    # Store messages
    store_messages(message_decoded, chat_response)

    print(chat_response)

    return "Done"
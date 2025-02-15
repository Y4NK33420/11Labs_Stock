from fastapi import FastAPI, WebSocket, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from twilio.twiml.voice_response import VoiceResponse, Connect
import json
import traceback
import os
from api.stock import router as stock_router
from api.twilio.voice import router as twilio_voice_router  # Use the Twilio router from voice.py
from api.search import router as search_router
from elevenlabs import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
# from .audio_interface import TwilioAudioInterface

app = FastAPI(title="Stock Market API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(stock_router)
app.include_router(twilio_voice_router)  # Use unified Twilio endpoints from voice.py
app.include_router(search_router)

@app.get("/")
async def root():
    return {
        "message": "Stock Market API is running",
        "docs_url": "/docs",
        "endpoints": {
            "stock_price": "/api/stock/price",
            "stock_history": "/api/stock/history",
            "market_summary": "/api/stock/market-summary",
            "twilio_webhook": "/inbound_call",
            "search": "/api/search"
        }
    }
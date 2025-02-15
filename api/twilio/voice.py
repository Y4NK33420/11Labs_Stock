from fastapi import APIRouter, Request, WebSocket
from fastapi.responses import HTMLResponse
from twilio.twiml.voice_response import VoiceResponse, Connect
from starlette.websockets import WebSocketDisconnect
import json
import traceback
import os
from elevenlabs import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from .audio_interface import TwilioAudioInterface

router = APIRouter()

@router.post("/inbound_call")
async def handle_incoming_call(request: Request):
    """
    Handle incoming Twilio call:
    - Extracts call details from the request
    - Creates a TwiML response that instructs Twilio to stream audio
      to our WebSocket endpoint
    """
    form_data = await request.form()
    call_sid = form_data.get("CallSid", "Unknown")
    from_number = form_data.get("From", "Unknown")
    print(f"Incoming call: CallSid={call_sid}, From={from_number}")

    response = VoiceResponse()
    connect = Connect()
    # Connect the call's audio stream to our WebSocket endpoint
    connect.stream(url=f"wss://{request.url.hostname}/media-stream")
    response.append(connect)
    return HTMLResponse(content=str(response), media_type="application/xml")

@router.websocket("/media-stream")
async def handle_media_stream(websocket: WebSocket):
    """
    Handles the WebSocket connection for audio streaming:
    - Accepts the WebSocket connection
    - Instantiates our Twilio audio interface
    - Starts a conversation session with the ElevenLabs agent
    - Processes incoming messages from Twilio
    """
    await websocket.accept()
    print("WebSocket connection established")

    audio_interface = TwilioAudioInterface(websocket)
    eleven_labs_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

    try:
        # Create the conversation with ElevenLabs agent
        conversation = Conversation(
            client=eleven_labs_client,
            agent_id=os.getenv("AGENT_ID"),
            requires_auth=True,
            audio_interface=audio_interface,
            callback_agent_response=lambda text: print(f"Agent: {text}"),
            callback_user_transcript=lambda text: print(f"User: {text}"),
        )

        conversation.start_session()
        print("Conversation session started")

        # Process incoming audio messages from Twilio
        async for message in websocket.iter_text():
            if not message:
                continue
            await audio_interface.handle_twilio_message(json.loads(message))

    except WebSocketDisconnect:
        print("WebSocket disconnected")
    except Exception:
        print("Error occurred in WebSocket handler:")
        traceback.print_exc()
    finally:
        try:
            conversation.end_session()
            conversation.wait_for_session_end()
            print("Conversation session ended")
        except Exception:
            print("Error ending conversation session:")
            traceback.print_exc() 
from fastapi import APIRouter
from .voice import router as voice_router

router = APIRouter(prefix="/api/twilio")
router.include_router(voice_router)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.stock import router as stock_router
from api.twilio import router as twilio_router  # This comes from api/twilio/voice.py
from api.search import router as search_router

app = FastAPI(title="Stock Market API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers with appropriate prefixes
app.include_router(stock_router)
app.include_router(twilio_router, prefix="/api/twilio")  # Added prefix to correctly map endpoints
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
            "twilio_webhook": "/api/twilio/inbound_call",
            "search": "/api/search"
        }
    }
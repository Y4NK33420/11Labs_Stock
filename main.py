from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.stock import router as stock_router
from api.twilio import router as twilio_router  
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

# Include routers without adding duplicate prefixes
app.include_router(stock_router)
app.include_router(twilio_router)  # Routes: /api/twilio/inbound_call and /api/twilio/media-stream as defined in voice.py
app.include_router(search_router)  # Route: /api/search

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
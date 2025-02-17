from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.stock import router as stock_router
from api.search import router as search_router   

app = FastAPI(title="Stock Market API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(stock_router)
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
            "stock_news": "/api/stock/vantage/news",
            "market_movers": "/api/stock/vantage/market-movers",
            "search": "/api/search"
        }
    }
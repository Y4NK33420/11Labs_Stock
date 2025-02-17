from fastapi import APIRouter, Query, HTTPException
import requests
import os

router = APIRouter()
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

@router.get("/news")
async def get_stock_news(
    tickers: str = Query(None, description="Comma-separated stock symbols"),
    topics: str = Query(None, description="Comma-separated news topics"),
    limit: int = Query(50, description="Number of news items to return")
):
    """Get news sentiment for stocks"""
    try:
        params = {
            "function": "NEWS_SENTIMENT",
            "apikey": ALPHA_VANTAGE_API_KEY,
            "limit": limit
        }
        if tickers:
            params["tickers"] = tickers
        if topics:
            params["topics"] = topics

        response = requests.get("https://www.alphavantage.co/query", params=params)
        data = response.json()
        
        if "feed" not in data:
            raise HTTPException(status_code=500, detail="Invalid response from Alpha Vantage API")
            
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch news data: {str(e)}")

@router.get("/market-movers")
async def get_market_movers():
    """Get top gainers, losers, and most actively traded stocks"""
    try:
        params = {
            "function": "TOP_GAINERS_LOSERS",
            "apikey": ALPHA_VANTAGE_API_KEY
        }
        
        response = requests.get("https://www.alphavantage.co/query", params=params)
        data = response.json()
        
        if "top_gainers" not in data or "top_losers" not in data:
            raise HTTPException(status_code=500, detail="Invalid response from Alpha Vantage API")
            
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch market movers: {str(e)}")

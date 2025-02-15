from fastapi import APIRouter, HTTPException
import yfinance as yf

router = APIRouter()

@router.get("")
async def get_market_summary():
    """Get summary of major market indices"""
    indices = ['^GSPC', '^DJI', '^IXIC']  # S&P 500, Dow Jones, NASDAQ
    summary = {}
    
    try:
        for index in indices:
            ticker = yf.Ticker(index)
            info = ticker.info
            summary[index] = {
                "name": info.get("shortName", "N/A"),
                "price": info.get("regularMarketPrice", "N/A"),
                "change": info.get("regularMarketChangePercent", "N/A"),
                "previous_close": info.get("regularMarketPreviousClose", "N/A")
            }
        return summary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch market summary: {str(e)}") 
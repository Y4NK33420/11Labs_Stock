from fastapi import APIRouter, Query, HTTPException
import yfinance as yf

router = APIRouter()

@router.get("")
async def get_stock_price(symbol: str = Query(..., description="The stock symbol to look up")):
    """Get current stock price and basic information"""
    try:
        stock = yf.Ticker(symbol)
        info = stock.info
        
        return {
            "symbol": symbol,
            "price": info.get("currentPrice", "N/A"),
            "currency": info.get("currency", "USD"),
            "company_name": info.get("longName", "N/A"),
            "market_cap": info.get("marketCap", "N/A"),
            "exchange": info.get("exchange", "N/A")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch stock data for {symbol}: {str(e)}") 
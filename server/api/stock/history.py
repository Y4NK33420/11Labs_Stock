from fastapi import APIRouter, Query, HTTPException
import yfinance as yf

router = APIRouter()

@router.get("")
async def get_stock_history(
    symbol: str = Query(..., description="The stock symbol to look up"),
    period: str = Query("1d", description="Time period for historical data")
):
    """Get historical stock data"""
    try:
        stock = yf.Ticker(symbol)
        history = stock.history(period=period)
        
        if not history.empty:
            latest = history.iloc[-1]
            return {
                "symbol": symbol,
                "period": period,
                "open": float(latest["Open"]),
                "high": float(latest["High"]),
                "low": float(latest["Low"]),
                "close": float(latest["Close"]),
                "volume": int(latest["Volume"])
            }
        else:
            raise HTTPException(status_code=404, detail=f"No historical data found for {symbol}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch historical data for {symbol}: {str(e)}") 
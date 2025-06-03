# Stock Market API

A FastAPI-based REST API for fetching stock market data, news, and performing market-related searches.

## Project Structure

```
11Labs_Stock/
├── api/
│   ├── stock/                 # Stock-related endpoints
│   │   ├── __init__.py       # Router configuration
│   │   ├── price.py          # Real-time price endpoints
│   │   ├── history.py        # Historical data endpoints
│   │   ├── market_summary.py # Market overview endpoints
│   │   └── vantage.py        # Alpha Vantage integration
│   └── search/               # Search functionality
│       ├── __init__.py       # Search router configuration
│       └── search.py         # Search implementation
├── main.py                   # Application entry point
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables
└── .env.example             # Environment template
```

## Core Components

### Main Application (main.py)
- Initializes FastAPI application
- Configures CORS middleware
- Mounts all routers
- Provides API documentation endpoint (/docs)

### Stock API Module (api/stock/)
1. **Price Module**
   - Real-time stock price queries
   - Current market data

2. **History Module**
   - Historical stock data
   - Time series analysis

3. **Market Summary Module**
   - Overall market indicators
   - Market indices

4. **Vantage Module**
   - News sentiment analysis
   - Market movers (top gainers/losers)
   - Uses Alpha Vantage API integration

### Search Module (api/search/)
- General market information search
- News search functionality
- Uses SerpAPI for comprehensive results

## API Flow

1. **Request Flow**
   ```
   Client Request → FastAPI Router → Specific Module → External API → Response
   ```

2. **Data Flow**
   - Client makes request to endpoint
   - Router directs to appropriate handler
   - Handler processes request and calls external APIs if needed
   - Data is formatted and returned to client

## Available Endpoints

- `/api/stock/price` - Get real-time stock prices
- `/api/stock/history` - Fetch historical data
- `/api/stock/market-summary` - Get market overview
- `/api/stock/vantage/news` - Get stock-related news
- `/api/stock/vantage/market-movers` - Get top market movers
- `/api/search` - General market search functionality

## Environment Setup

1. Copy `.env.example` to `.env`
2. Add your API keys:
   - ALPHA_VANTAGE_API_KEY
   - SERPAPI_API_KEY

## Running the Application

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

3. Access the API documentation :
   ```
   http://localhost:3000/docs
   ```

## The corresponding websocket server code for Twilio connection can be found at https://github.com/Y4NK33420/twilio_js

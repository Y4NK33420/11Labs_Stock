from fastapi import APIRouter
from .price import router as price_router
from .history import router as history_router
from .market_summary import router as market_summary_router
from .vantage import router as vantage_router

router = APIRouter()

# Simple route mounting without redundant prefixes
router.include_router(price_router, prefix="/price")
router.include_router(history_router, prefix="/history")
router.include_router(market_summary_router, prefix="/market-summary")
router.include_router(vantage_router, prefix="/vantage")
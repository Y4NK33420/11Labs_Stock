from fastapi import APIRouter
from .price import router as price_router
from .history import router as history_router
from .market_summary import router as market_summary_router

router = APIRouter(prefix="/api/stock")

router.include_router(price_router, prefix="/price")
router.include_router(history_router, prefix="/history")
router.include_router(market_summary_router, prefix="/market-summary") 
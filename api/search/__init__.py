from fastapi import APIRouter
from .search import router as search_router

router = APIRouter(prefix="/api/search")
router.include_router(search_router) 
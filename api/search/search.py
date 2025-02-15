from fastapi import APIRouter, Query, HTTPException
from serpapi import GoogleSearch
import os

router = APIRouter()

@router.get("")
async def search_news(
    query: str = Query(..., description="The search query"),
    num_results: int = Query(5, description="Number of results to return", ge=1, le=10)
):
    """Search for news and information"""
    try:
        search = GoogleSearch({
            "q": query,
            "num": num_results,
            "api_key": os.getenv("SERPAPI_API_KEY")
        })
        results = search.get_dict()
        
        # Extract organic results
        if "organic_results" in results:
            formatted_results = []
            for result in results["organic_results"][:num_results]:
                formatted_results.append({
                    "title": result.get("title", ""),
                    "link": result.get("link", ""),
                    "snippet": result.get("snippet", ""),
                    "source": result.get("source", "")
                })
            return {"results": formatted_results}
        else:
            return {"results": [], "message": "No results found"}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to perform search: {str(e)}") 
from fastapi import APIRouter
from servicies import movie_service
import requests

router = APIRouter()

router = APIRouter(
    prefix="/movie",
    tags=["movie"],
    responses={404: {"description": "Not found"}},
)

ms = movie_service()

@router.get("/search")
async def movie_search(query: str):
    movie_found = ms.search_movie(query)
    return movie_found

@router.get("/watch_providers")
async def movie_watch_providers(id, country_code):
    watch_providers = ms.get_watch_providers(id, country_code)

    if watch_providers == None:
        return None #Ver de como tirar un 404 u otra clase de error
        
    elif watch_providers is not None:
        return watch_providers
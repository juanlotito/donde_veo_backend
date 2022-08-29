from fastapi import APIRouter
from servicies import movie_service

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
    return watch_providers
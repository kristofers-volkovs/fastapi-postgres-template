from fastapi import APIRouter, FastAPI
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware

from src.main.health import health_router
from src.main.settings import settings

server = FastAPI(
    default_response_class=ORJSONResponse,
    title="Template API",
    version="0.0.1",
)

server.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
)

api_router = APIRouter()
api_router.include_router(health_router)

server.include_router(api_router, prefix=settings.API_V1_STR)

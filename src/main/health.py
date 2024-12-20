from fastapi import APIRouter
from pydantic import BaseModel

health_router = APIRouter(tags=["Health"])


class HealthRsp(BaseModel):
    is_healthy: bool


@health_router.get(
    "/health",
    response_model=HealthRsp,
)
def get_health() -> HealthRsp:
    return HealthRsp(is_healthy=True)

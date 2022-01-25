from enum import Enum
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class HealthStatus(str, Enum):
    ALIVE = 'alive'

class GetHealthOut(BaseModel):
    status: HealthStatus

@router.get('/health', response_model=GetHealthOut)
def get_health():
    return GetHealthOut(status=HealthStatus.ALIVE)
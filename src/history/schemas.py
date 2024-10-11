from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from .models import Measure
from ..auth.models import User

class MeasureBase(BaseModel):
    downloadSpeed: str
    uploadSpeed: str
    coordinates: str

class MeasureResponse(BaseModel):
    username: str
    downloadSpeed: str
    uploadSpeed: str
    coordinates: str
    created_at: Optional[datetime] = datetime.now()

class UserById(BaseModel):
    id: int
    email: str
    username: str

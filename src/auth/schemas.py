from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    id: Optional[int] = None
    email: str
    username: str
    password: str
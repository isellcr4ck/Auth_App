from fastapi import APIRouter
from pydantic import EmailStr
from .schemas import UserBase
from . import crud
from .models import User

SESSION = crud.init_db()

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login(email: EmailStr, password: str):
    user_query = SESSION.query(User).filter_by(email=email).first()
    if not user_query:
        return {"error": "Invalid email or password"}
    if not crud.verify_pass(password, user_query.password):
        return {"error": "Invalid email or password"}
    return {"id": user_query.id}


@router.post("/register")
async def register(email: EmailStr, username: str, password: str):
    password = crud.hash_password(password)
    user = User(email=email, username=username, password=password)
    SESSION.add(user)
    SESSION.commit()
    return {"id": user.id}
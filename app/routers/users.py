from fastapi import APIRouter, HTTPException, status
from app.schemas import UserCreate, UserOut
from app.db import db, get_user_by_username, add_user

router = APIRouter()

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    existing_user = await get_user_by_username(user.username)
    if existing_user:
        raise HTTPException(status_code=409, detail="Username already exists.")
    user_obj = await add_user(user)
    return user_obj

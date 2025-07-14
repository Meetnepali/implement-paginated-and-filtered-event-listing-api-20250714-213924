from fastapi import Header, HTTPException, status, Depends
from app.db import get_user_by_username
import asyncio

async def get_current_user(x_username: str = Header(...)):
    user = await get_user_by_username(x_username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized. Register first.")
    return user

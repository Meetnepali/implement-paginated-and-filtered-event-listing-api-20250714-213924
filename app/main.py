from fastapi import FastAPI
from app.routers import users, reservations
from app.errors import register_exception_handlers

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(reservations.router, prefix="/reservations", tags=["reservations"])

register_exception_handlers(app)

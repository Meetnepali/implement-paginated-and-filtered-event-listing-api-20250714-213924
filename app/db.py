import asyncio
from app.schemas import UserCreate, UserOut, Book

# Simulate async DB with in-memory dict
# db["users"]: list of dicts {id, username, password}
# db["books"]: list of dicts {id, title, available}
# db["reservations"]: list of dicts {id, user_id, book_id}
db = {
    "users": [],
    "books": [
        {"id": 1, "title": "The Great Gatsby", "available": True},
        {"id": 2, "title": "1984", "available": True},
    ],
    "reservations": []
}

async def get_user_by_username(username: str):
    await asyncio.sleep(0)
    for user in db["users"]:
        if user["username"] == username:
            return user
    return None

async def add_user(user: UserCreate):
    new_id = len(db["users"]) + 1
    user_obj = {"id": new_id, "username": user.username, "password": user.password}
    db["users"].append(user_obj)
    return {"id": user_obj["id"], "username": user_obj["username"]}

async def get_book_by_id(book_id: int):
    await asyncio.sleep(0)
    for book in db["books"]:
        if book["id"] == book_id:
            return book
    return None

async def add_reservation(reservation, user):
    rid = len(db["reservations"]) + 1
    reservation_obj = {"id": rid, "user_id": user["id"], "book_id": reservation.book_id}
    db["reservations"].append(reservation_obj)
    return reservation_obj

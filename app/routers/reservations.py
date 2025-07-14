from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import ReservationCreate, ReservationOut
from app.db import db, get_book_by_id, add_reservation, get_user_by_username
from app.dependencies import get_current_user

router = APIRouter()

@router.post("/", response_model=ReservationOut, status_code=status.HTTP_201_CREATED)
async def reserve_book(
    reservation: ReservationCreate,
    current_user=Depends(get_current_user)
):
    book = await get_book_by_id(reservation.book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found.")
    # Simplified: allow single reservation per book per user.
    for existing in db["reservations"]:
        if existing["book_id"] == reservation.book_id and existing["user_id"] == current_user["id"]:
            raise HTTPException(status_code=409, detail="You already reserved this book.")
    reservation_obj = await add_reservation(reservation, current_user)
    return reservation_obj

from pydantic import BaseModel, Field, constr, validator
from typing import Optional

USERNAME_REGEX = r'^[a-zA-Z0-9._-]{3,16}$'
PASSWORD_REGEX = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$'

class UserCreate(BaseModel):
    username: constr(regex=USERNAME_REGEX)
    password: constr(min_length=6, max_length=32, regex=PASSWORD_REGEX)

    @validator('username')
    def username_no_spaces(cls, v):
        if ' ' in v:
            raise ValueError('No spaces allowed in username')
        return v

class UserOut(BaseModel):
    id: int
    username: str

class ReservationCreate(BaseModel):
    book_id: int = Field(..., gt=0)

class ReservationOut(BaseModel):
    id: int
    user_id: int
    book_id: int

class Book(BaseModel):
    id: int
    title: str
    available: bool

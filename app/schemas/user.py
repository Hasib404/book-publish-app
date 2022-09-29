from typing import Optional, List

from pydantic import BaseModel, EmailStr
from schemas.books import Book


class Login(BaseModel):
    username: Optional[str]
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True


class TokenUser(Token):
    pass


class TokenData(BaseModel):
    username: Optional[str] = None


class UserInDBBase(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    name: Optional[str] = None
    author_pseudonym: Optional[str] = None

    class Config:
        orm_mode = True


# Properties to receive via API on creation
class UserCreate(UserInDBBase):
    name: str
    password: str
    author_pseudonym: str


# Properties to receive via API on update
class UserUpdate(UserInDBBase):
    id: int
    password: Optional[str] = None


# Properties to return to client
class User(UserInDBBase):
    id: int
    name: str
    author_pseudonym: str
    book_list: List[Book]


class UserDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional


class BookinDBBase(BaseModel):
    title: str

    class Config:
        orm_mode = True


# Properties to receive via API on creation
class BookCreate(BookinDBBase):
    description: str
    cover_image: str
    price: int
    author_id: int


# Properties to receive via API on update
class BookUpdate(BaseModel):
    id: int
    author_id: Optional[int]
    title: Optional[str]
    description: Optional[str]
    cover_image: Optional[str]
    price: Optional[int]

    class Config:
        orm_mode = True


# Properties to return to client
class Book(BaseModel):
    id: int
    author_id: int
    title: str
    description: str
    cover_image: str
    price: int

    class Config:
        orm_mode = True


class BookDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True

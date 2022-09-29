from dataclasses import field
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from typing import Union, List

from db.session import get_db
from models.books import Books
from .service import book_service
from schemas.books import BookCreate, Book, BookDelete, BookUpdate
from schemas.user import UserCreate
from api.deps import get_current_active_user
from api.user.controller import are_you_darth_vader

router = APIRouter()


@router.get("/book/{id}", response_model=Book, tags=["book"])
def get_book(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_current_active_user),
):
    return book_service.get(db, id)


@router.get("/books", response_model=List[Book], tags=["book"])
def get_all_books(title: Union[str, None] = None, db: Session = Depends(get_db)):
    if title is None:
        return book_service.get_multi(db)
    else:
        field = "title"
        return book_service.get_multi_by_field(db, field=field, value=title)


@router.post("/book/publish", response_model=Book, status_code=201, tags=["book"])
def publish_book(
    book: BookCreate,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_current_active_user),
):
    if are_you_darth_vader(current_user.name, current_user.author_pseudonym):
        raise HTTPException(status_code=400, detail=f"You are not welcome")
    elif book.author_id is not current_user.id:
        raise HTTPException(status_code=400, detail=f"No author found")
    else:
        return book_service.create(db, obj_in=book)


@router.put("/book/update/{id}", response_model=Book, tags=["book"])
def update_book(
    upd_user: BookUpdate,
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_current_active_user),
):
    book = (
        db.query(Books).filter(Books.id == id, Books.author_id == current_user.id).all()
    )
    if not book:
        raise HTTPException(status_code=400, detail=f"Book not found")
    return book_service.update(db, obj_in=upd_user)


@router.delete("/book/unpublish/{id}", response_model=BookDelete, tags=["book"])
def unpublish_book(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_current_active_user),
):
    book = (
        db.query(Books).filter(Books.id == id, Books.author_id == current_user.id).all()
    )
    if not book:
        raise HTTPException(status_code=400, detail=f"Book not found")
    else:
        return book_service.remove(db, id=id)

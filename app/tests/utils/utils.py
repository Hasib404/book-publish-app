from typing import Optional
import string
import random

from api.user.service import user_service
from api.book.service import book_service
from schemas.user import UserCreate
from schemas.books import BookCreate


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=16))


def create_user(db, password: Optional[str] = None):
    user_in_create = UserCreate(
        username="johndoe",
        name="John Smith",
        email="john@test.com",
        password=password,
        author_pseudonym="John Doe",
    )
    return user_service.create(db, obj_in=user_in_create)


def create_book(db, id: Optional[int] = None):
    book_in_create = BookCreate(
        title=random_lower_string(),
        description=random_lower_string(),
        cover_image=f"http://{random_lower_string()}/{random_lower_string()}.jpg",
        price=20.00,
        author_id=id,
    )
    return book_service.create(db, obj_in=book_in_create)


def generate_access_token(client, username: str, password: str) -> None:
    data = {"username": username, "password": "password"}
    response = client.post("/login/", json=data)
    content = response.json()
    return content["access_token"]

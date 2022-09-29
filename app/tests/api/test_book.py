from tests.utils.utils import create_user, generate_access_token, create_book

from api.user.service import user_service
from schemas.user import UserCreate


def test_publish_book(db, client) -> None:
    response = create_user(db, password="password")
    username = response.username
    password = response.password
    access_token = generate_access_token(client, username, password)
    headers = {"token": access_token}
    publish_book = {
        "title": "Hills",
        "description": "Scary story",
        "cover_image": "http://abc.com/cover.jpg",
        "price": 20.00,
        "author_id": response.id,
    }
    response = client.post("/book/publish", headers=headers, json=publish_book)
    assert 200 <= response.status_code < 300


def test_darth_vader_publish_book(db, client) -> None:
    user_in_create = UserCreate(
        username="darth1",
        name="Darth Vader",
        email="darth@test.com",
        password="password",
        author_pseudonym="Darth Vader",
    )
    response = user_service.create(db, obj_in=user_in_create)
    username = response.username
    password = response.password
    access_token = generate_access_token(client, username, password)
    headers = {"token": access_token}
    publish_book = {
        "title": "Hills",
        "description": "Scary story",
        "cover_image": "http://abc.com/cover.jpg",
        "price": 20.00,
        "author_id": response.id,
    }
    response = client.post("/book/publish", headers=headers, json=publish_book)
    content = response.json()
    assert content["detail"] == "You are not welcome"
    assert 400 <= response.status_code < 500

def test_unpublish_book(db, client) -> None:
    user = create_user(db, password="password")
    username = user.username
    password = user.password
    access_token = generate_access_token(client, username, password)
    headers = {"token": access_token}
    book = create_book(db, user.id)
    response = client.delete(f"/book/unpublish/{book.id}", headers=headers)
    assert 200 <= response.status_code < 300
    assert response.json()["id"] == book.id


def test_booklist_of_an_author(db, client) -> None:
    response = create_user(db, password="password")
    create_book(db, response.id)
    create_book(db, response.id)
    create_book(db, response.id)
    response = client.get("/books")
    content = response.json()
    assert 200 <= response.status_code < 300
    assert len(content) == 3

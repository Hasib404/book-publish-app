from tests.utils.utils import create_user


def test_authentication_token_from_username(client, db) -> None:
    """
    Return a valid token for the user with given username.
    """
    username = "johndoe"
    password = "password"
    create_user(db, password)
    data = {"username": username, "password": password}
    response = client.post("/login/", json=data)
    content = response.json()
    assert 200 <= response.status_code < 300
    assert "access_token" in content
    assert content["access_token"]


def test_authentication_failure(client, db) -> None:
    """
    Return a valid token for the user with given username.
    """
    username = "johdoe"
    password = "password"
    create_user(db, password)
    data = {"username": username, "password": password}
    response = client.post("/login/", json=data)
    content = response.json()
    assert content["detail"] == "Incorrect username or password"
    assert response.status_code == 400


def test_create_user(client) -> None:
    payload = {
        "username": "janedoe",
        "email": "jane@test.com",
        "name": "Jane Smith",
        "password": "password",
        "author_pseudonym": "Jane Doe",
    }
    response = client.post("/user/create", json=payload)
    content = response.json()
    assert 200 <= response.status_code < 300
    assert content["email"] == "jane@test.com"

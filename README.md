# Book Store

A book publishing app where the user can create account and sell their adventures.

- [API Endpoints](#api-endpoints)
- [Error handling](#error-handling)
- [Install](#install)
- [Test api locally](#test-api-locally)
- [Run tests](#run-tests)

## API Endpoints

#### POST `/login/`

User can login with `username` and `password`, after successful authentication a JWT token will be created for further access of that logged in user.

**Request**

```
{
  "username": "string",
  "password": "string"
}
```

**Example Response**

```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NjE5MTgwNDMsInN1YiI6InN0cmluZyJ9.FfEP2dAkisDOwU1McX2vJUDda3tfDPAi3sVdHLY4i4w",
  "token_type": "bearer"
}
```

---

#### POST `/user/create`

This endpoint will create a new user.

**Request**

```
{
  "username": "string",
  "email": "user@example.com",
  "name": "string",
  "author_pseudonym": "string",
  "password": "string"
}
```

**Example Response**

```
{
  "username": "string",
  "email": "user@example.com",
  "name": "string",
  "author_pseudonym": "string",
  "id": 1,
  "book_list": []
}
```

---

#### GET `/user/{id}`

This endpoint will provide information of an authenticated user.

**Request**

```
Pass user id as param and jwt token as header.
```

**Example Response**

```
{
  "username": "string",
  "email": "user@example.com",
  "name": "string",
  "author_pseudonym": "string",
  "id": 1,
  "book_list": []
}
```

---

#### PUT `/user/update`

This endpoint will update the information of existing user with authentication.

**Request**

```
{
  "username": "string",
  "email": "user@example.com",
  "name": "updated string",
  "author_pseudonym": "string",
  "id": 1,
  "password": "string"
}
```

**Example Response**

```
{
  "username": "string",
  "email": "user@example.com",
  "name": "updated string",
  "author_pseudonym": "string",
  "id": 1,
  "book_list": []
}
```

---

#### DELETE `/user/delete/{id}`

This endpoint will delete an existing user.

**Request**

```
Pass user id as param and jwt token as header.
```

---

**Example Response**

```
{
  "id": 1,
}
```

---

#### POST `/book/publish`

This endpoint will publish a book under an existing user.

**Request**

```
{
  "title": "string",
  "description": "string",
  "cover_image": "http://images.com/image.jpg",
  "price": 20,
  "author_id": 1
}
```

**Example Response**

```
{
  "id": 1,
  "author_id": 1,
  "title": "string",
  "description": "string",
  "cover_image": "http://images.com/image.jpg",
  "price": 20
}
```

---

#### GET `/book/{id}`

This endpoint will provide information of a specific book.

**Request**

```
Pass book id as param and jwt token as header.
```

**Example Response**

```
{
  "id": 1,
  "author_id": 1,
  "title": "string",
  "description": "string",
  "cover_image": "http://images.com/image.jpg",
  "price": 20
}
```

---

#### PUT `/book/update/{id}`

This endpoint will update the information of existing user with authentication.

**Request**

```
{
  "id": 1,
  "author_id": 1,
  "title": "string",
  "description": "string",
  "cover_image": "http://images.com/image.jpg",
  "price": 200
}
```

**Example Response**

```
{
  "id": 1,
  "author_id": 1,
  "title": "string",
  "description": "string",
  "cover_image": "http://images.com/image.jpg",
  "price": 200
}
```

---

#### DELETE `/book/unpublish/{id}`

This endpoint will delete an existing book of specific author.

**Request**

```
Pass book id as param and jwt token as header.
```

**Example Response**

```
{
  "id": 1,
}
```

---

#### GET `/books`

This endpoint will provide all the published books.

**Request**

```
Query parameter can be passed as `title` to search book by title or without query parameter all the books will be returned.
```

**Example Response**

```
[
  {
    "id": 1,
    "author_id": 1,
    "title": "string",
    "description": "string",
    "cover_image": "http://images.com/image.jpg",
    "price": 200
  }
]
```

---

## Error handling

- 201 - Created
- 400 - Bad Request
- 500 - Internal Server Error

---

## Install

- A `dockerfile` for backend server added.
- A `docker-compose.yml` file consists of 2 services `api` & `db` added.
- A `docker-compose-test.yml` file added providing information for test database.

To run api, execute the following command:

```

docker compose up -d --build --force-recreate; docker-compose run api python3 -m alembic.config upgrade head

```

(It will force to be recreated) and folloing that alembic migration will run to create the tables.

---

## Test api locally

To test the system follow the steps,

1. First install the app using docker
2. Then check `http://localhost/docs` on your browser to find a beautiful Swagger API documentation provided by FastAPI.
3. After that test the endpoints.

---

## Run tests

To run tests, follow the steps,

```

docker compose -f docker-compose-test.yml up -d --build --force-recreate; virtualenv venv; source venv/bin/activate; cd app; pip install -r requirements.txt; python -m pytest -v

```

Above command will be following the steps under the hood

1. It will force db to be recreated
2. A virtual environment will be initialized.
3. Virtual environment will be activated.
4. Requirements will be installed.
5. Atlast it will run the tests.

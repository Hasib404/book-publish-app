from sqlalchemy.orm import Session
from models.books import Books
from fastapi import APIRouter, Depends, HTTPException
from db.session import get_db
from api.user.service import user_service
from schemas.user import Login, TokenUser, UserCreate, UserUpdate, User, UserDelete

from utils.security import create_access_token
from api.user.controller import authenticate
from api.deps import get_current_active_user


router = APIRouter()


@router.post("/login/", response_model=TokenUser, tags=["auth"])
def login(user: Login, db: Session = Depends(get_db)) -> TokenUser:
    user_auth = authenticate(db, username=user.username, password=user.password)
    if not user_auth:
        raise HTTPException(status_code=400, detail=f"Incorrect username or password")
    return {
        "access_token": create_access_token(user_auth.username),
        "token_type": "bearer",
    }


@router.get("/user/{id}", response_model=User, tags=["user"])
def get_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_current_active_user),
):
    if id is not current_user.id:
        raise HTTPException(status_code=400, detail=f"No user found")
    return user_service.get(db, id)


@router.post("/user/create", response_model=User, status_code=201, tags=["user"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create(db, obj_in=user)


@router.delete("/user/delete/{id}", response_model=UserDelete, tags=["user"])
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_current_active_user),
):
    return user_service.remove(db, id=id)


@router.put("/user/update", response_model=User, tags=["user"])
def update_user(
    upd_user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: UserCreate = Depends(get_current_active_user),
):
    if upd_user.id is not current_user.id:
        raise HTTPException(status_code=400, detail=f"No user found")
    return user_service.update(db, obj_in=upd_user)

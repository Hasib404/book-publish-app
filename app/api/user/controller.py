from typing import Optional

from sqlalchemy.orm import Session

from utils.security import verify_password
from api.user.service import user_service


def authenticate(db: Session, *, username: Optional[str] = None, password: str):
    user = user_service.get_by_field(db, field="username", value=username)

    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


def are_you_darth_vader(name, author_pseudonym):
    if name == "Darth Vader" or author_pseudonym == "Darth Vader":
        return True
    else:
        return False

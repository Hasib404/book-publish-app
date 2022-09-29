from fastapi import APIRouter

from .user import user
from .book import books

router = APIRouter()
router.include_router(user.router)
router.include_router(books.router)

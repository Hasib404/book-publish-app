from sqlalchemy.orm import Session
from typing import Union, Dict, Any
from fastapi.encoders import jsonable_encoder

from models.books import Books
from db.crud import CRUDBase
from schemas.books import Book, BookCreate, BookUpdate


class CRUDUser(CRUDBase[Book, BookCreate, BookUpdate]):
    def create(self, db: Session, *, obj_in: BookCreate) -> Books:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, obj_in: Union[BookUpdate, Dict[str, Any]]
    ) -> Books:
        db_obj = db.query(self.model).get(obj_in.id)
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            setattr(db_obj, field, update_data[field])

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


book_service = CRUDUser(model=Books)

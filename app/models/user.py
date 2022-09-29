from db.base_class import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Users(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(25), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(256), nullable=False)
    author_pseudonym = Column(String(256), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    book_list = relationship(
        "Books",
        cascade="all,delete-orphan",
        back_populates="author",
        uselist=True,
    )

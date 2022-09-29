from sqlalchemy import Column, Integer, Numeric, String, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Books(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(256), unique=True, nullable=False)
    description = Column(String(256), unique=True, nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    author = relationship("Users", back_populates="book_list")
    cover_image = Column(String(256), index=True, nullable=True)
    price = Column(Numeric(5, 2))

from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .user import User


class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    contents = Column(String)
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="posts")


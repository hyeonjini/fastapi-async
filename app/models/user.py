from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .post import Post  # noqa


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    password = Column(String, nullable=False)
    posts = relationship("Post", back_populates="author")

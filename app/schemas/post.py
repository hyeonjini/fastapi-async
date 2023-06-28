from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    title: Optional[str]
    contents: Optional[str]
    author_id: Optional[int]


class PostCreate(PostBase):
    title: str
    contents: str
    author_id: int


class PostUpdate(PostBase):
    title: str
    contents: str


class PostInDBBase(PostBase):
    id: Optional[int]

    class Config:
        orm_mode = True


class Post(PostInDBBase):
    pass

from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    name: Optional[str] = None
    password: Optional[str] = None


class UserCreate(UserBase):
    name: str
    password: str


class UserUpdate(UserBase):
    name: str
    password: str


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    pass

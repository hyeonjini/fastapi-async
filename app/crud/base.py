from typing import Any, Dict, Optional, Generic, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

# from sqlalchemy.orm import Session

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.base_class import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        async with db.begin() as db:
            result = (
                await db.query(self.model).filter(self.model.id == id).first()
            )
            return result

    async def get_multi(
        self, db: AsyncSession, *, skip: int = 0, limit: int = 100
    ):
        async with db.begin() as db:
            return await db.query(self.model).offset(skip).limit(limit).all()

    # def get(self, db: Session, id: Any) -> Optional[ModelType]:
    #     return db.query(self.model).filter(self.model.id == id).first()

    # def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100):
    #     return db.query(self.model).offset(skip).limit(limit).all()

    async def create(
        self, db: AsyncSession, *, obj_in: CreateSchemaType
    ) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)  # noqa
        db_obj = self.model(**obj_in_data)  # noqa
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    # def update(
    #     self,
    #     db: Session,
    #     *,
    #     db_obj: ModelType,
    #     obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    # ) -> ModelType:
    #     pass

    # def remove(self, db: Session, *, id: int) -> ModelType:
    #     pass

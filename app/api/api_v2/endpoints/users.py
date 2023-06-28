from typing import Optional, Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, models, schemas
from app.api import deps


router = APIRouter()


@router.get("/{name}", response_model=Optional[schemas.User])
async def read_user(
    db: AsyncSession = Depends(deps.get_db), id: int = None
) -> Any:
    user = await crud.user.get(db, id)

    if not user:
        pass

    return user


@router.get("/", response_model=List[schemas.User])
async def read_users(
    db: AsyncSession = Depends(deps.get_db), skip: int = 10, limit: int = 100
) -> Any:
    users = await crud.user.get_multi(db, skip=skip, limit=limit)
    return users

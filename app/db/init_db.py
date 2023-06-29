import random
import string

from sqlalchemy.ext.asyncio import AsyncSession

from app import crud, schemas


async def init_db(db: AsyncSession) -> None:
    for _ in range(10000):
        await create_random_user(db)


async def create_random_user(db: AsyncSession):
    user_create = schemas.UserCreate(
        name=random_lower_string(), password=random_lower_string()
    )
    await crud.user.create(db, obj_in=user_create)


def random_lower_string() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=10))

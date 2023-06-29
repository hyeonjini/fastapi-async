from typing import Generator

from app.db.session import async_session

# from app.db.session import SessionLocal


async def get_db() -> Generator:
    async with async_session() as session:
        yield session


# def get_db() -> Generator:
#     try:
#         session = SessionLocal()
#         yield session

#     finally:
#         session.close()

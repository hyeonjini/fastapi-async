import asyncio
from app.db.session import async_session
from app.db.init_db import init_db


async def main():
    db = async_session()
    await init_db(db)


if __name__ == "__main__":
    asyncio.run(main())

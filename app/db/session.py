# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.core.config import settings

# engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

engine = create_async_engine(
    settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True
)
async_session = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

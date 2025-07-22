from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

from config import (
    DATABASE_HOST,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_USER,
)


Base = declarative_base()

SQLALCHEMY_DATABASE_URL = f"mysql+asyncmy://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"


engine = create_async_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
session_local = async_sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

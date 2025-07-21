from typing import AsyncIterator

from sqlalchemy.ext.asyncio.session import AsyncSession

from .connection import engine, session_local
from .schema import *


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_db() -> AsyncIterator[AsyncSession]:
    session = session_local()
    try:
        yield session
    except Exception:
        await session.rollback()
        raise
    finally:
        await session.close()

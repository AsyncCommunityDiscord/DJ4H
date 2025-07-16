from sqlalchemy import Column, Integer
from sqlalchemy.sql.schema import PrimaryKeyConstraint

from .connection import Base


class Guild(Base):
    __tablename__ = "guilds"

    id = Column(Integer, autoincrement=True)
    guild_id = Column(Integer, unique=True, nullable=False)
    channel_id = Column(Integer, nullable=False)

    __table_args__ = (PrimaryKeyConstraint("guild_id", "channel_id"),)

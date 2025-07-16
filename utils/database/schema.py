from sqlalchemy import BigInteger, Column

from .connection import Base


class Guild(Base):
    __tablename__ = "guilds"

    guild_id = Column(BigInteger, primary_key=True, unique=True, nullable=False)
    channel_id = Column(BigInteger, primary_key=True, nullable=False)
    delay_second = Column(BigInteger, nullable=False)

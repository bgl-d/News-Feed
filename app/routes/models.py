# for classes and database manegment
from sqlalchemy import String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = "posts"

    post_id: Mapped[int] = mapped_column(primary_key=True)
    author_handle: Mapped[str] = mapped_column(String(50))
    title: Mapped[str] = mapped_column(String(50))
    text_content: Mapped[str] = mapped_column(String(200))
    media_storage_key: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
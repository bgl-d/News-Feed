# for classes and database manegment
from sqlalchemy import String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"

    post_id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[str] = mapped_column(String(100))
    title: Mapped[str] = mapped_column(String(100))
    text_content: Mapped[str] = mapped_column(String(500))
    media_link: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


class User(Base):
    __tablename__ = 'users'

    user_id: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    password_hash: Mapped[str] = mapped_column(String(100))


class Followers(Base):
    __tablename__ = 'followers'

    user_id: Mapped[str] = mapped_column(primary_key=True)
    following: Mapped[str] = mapped_column(primary_key=True)


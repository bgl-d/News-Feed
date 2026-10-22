# for classes and database manegment
from sqlalchemy import String, func, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()


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


def get_connection():
    try:
        engine = create_engine(f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")
        with engine.connect():
            pass
        print('Connection to the database created successfully.')
        return engine
    except Exception as ex:
        print('Connection failed due to the following error:\n', ex)

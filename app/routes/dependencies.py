# for classes and database manegment
from sqlalchemy import String, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime
import psycopg2
import os
from dotenv import load_dotenv


load_dotenv()

class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "posts"

    post_id: Mapped[int] = mapped_column(primary_key=True)
    author_handle: Mapped[str] = mapped_column(String(10))
    title: Mapped[str] = mapped_column(String(20))
    text_content: Mapped[str] = mapped_column(String(200))
    media_storage_key: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())


def get_connection():
    try:
        return psycopg2.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
        )
    except:
        return False

conn = get_connection()
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")

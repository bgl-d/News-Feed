# for classes and database manegment
from sqlalchemy import Column, Integer, String, Text, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts',
    id = Column(Integer, primary_key=True, index=True),
    url = Column(String, nullable=False)
    title = Column(String),
    text = Column (Text),
    media_storage_key = Column (String),
    author_id = Column(Integer, nullable=False),
    published_at = Column(Time)
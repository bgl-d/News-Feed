from sqlalchemy import Column, Integer, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Post():
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    text = Column (Text)
    user_id = Column(Integer, nullable=False)
    storage_key = Column (Text, nullable=False)

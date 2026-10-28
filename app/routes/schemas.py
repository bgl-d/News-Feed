from pydantic import BaseModel, Field


class PostCreate(BaseModel):
    title: str = Field(max_length=50)
    text_content: str = Field(max_length=200)
    media_link: str

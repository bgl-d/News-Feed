from fastapi import APIRouter

feed = APIRouter()

@feed.get('/feed')
async def read_posts():
    ...

@feed.get('/feed/{item_id}')
async def read_item(item_id: int):
    ...

@feed.put('/feed/create_post')
async def create_post(text: str, media_link: str):
    ...


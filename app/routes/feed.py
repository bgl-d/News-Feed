from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from models import Base, Post
from database import get_db, engine


feed = APIRouter()
templates = Jinja2Templates(directory='templates')
feed.mount('/static', StaticFiles(directory='static'), name='static')
feed.mount("/media", StaticFiles(directory="media"), name="media")
Base.metadata.create_all(engine)


@feed.get('/')
def home_redirect():
    return RedirectResponse(url="/feed")


@feed.get('/feed')
def home(request: Request):
    return templates.TemplateResponse(
        name='feed.html',
        request=request
    )  


@feed.get('/api/load_posts', response_model=list[Post])
def build_feed():
    return [
        {"title": "Nobel Prize 2026 in Physics", "text": "Franz Holsen", "mediaLink": "media/images/df7o6opc_nobel-price-in-physics-_650x400_06_October_26.jpg.webp"}
    ]


@feed.post('/api/create_post')
def post():
    post1 = Post(author_handle='', 
            title='', 
            text_content='', 
            media_storage_key='')
    return post1
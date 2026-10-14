from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

feed = APIRouter()

# Setup for Jinja2 templates
templates = Jinja2Templates(directory='templates')
feed.mount('/static', StaticFiles(directory='static'), name='static')
feed.mount("/media", StaticFiles(directory="media"), name="media")

@feed.get('/')
def home_redirect():
    return RedirectResponse(url="/feed")

@feed.get('/feed')
def home(request: Request):
    return templates.TemplateResponse(
        name='feed.html',
        request=request
    )
    

# @feed.get('/')
# def read_posts():
#     ...

# @feed.post('/feed/new-post')
# def create_post(text: str, media_link: str):
#     ...

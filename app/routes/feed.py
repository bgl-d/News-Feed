from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy import desc
from .models import Base, Post
from .database import get_db, engine
from .schemas import PostCreate


feed = APIRouter()
templates = Jinja2Templates(directory='templates')
feed.mount('/static', StaticFiles(directory='static'), name='static')
feed.mount("/media", StaticFiles(directory="media"), name="media")
Base.metadata.create_all(engine)


# Rewrite later to redirect to auth
@feed.get('/')
def home_redirect():
    return RedirectResponse(url="/feed")


@feed.get('/feed')
def home(request: Request):
    return templates.TemplateResponse(
        name='feed.html',
        request=request,
    )  


@feed.get('/load-posts/posts/{page_num}')
def build_feed(page_num: int, db: Session = Depends(get_db)):
    posts = (
        db.query(Post)
        .order_by(desc(Post.created_at))
        .limit(3)
        .offset((page_num-1)*3)
    )
    result = []
    for post in posts:
        item = {
            "title": post.title, 
            "text": post.text_content, 
            "media_link": post.media_link,
            "created_at": post.created_at.strftime("%d %b %Y")
        }
        result.append(item)
    return result


@feed.get('/load-posts/total-posts')
def build_feed(db: Session = Depends(get_db)):
    return db.query(Post).count()


@feed.post('/create-post')
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    new_post = Post(
        author_id='some_user',
        title=post.title,
        text_content=post.text_content,
        media_link=post.media_link,
    )
    db.add(new_post)
    db.flush()
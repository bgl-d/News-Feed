from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

auth = APIRouter()
templates = Jinja2Templates(directory='templates')
auth.mount('/static', StaticFiles(directory='static'), name='static')
auth.mount("/media", StaticFiles(directory="media"), name="media")

@auth.get('/auth')
async def authantification(request: Request):
    return templates.TemplateResponse(
        name='auth.html',
        request=request,
    )  

@auth.post('/auth/sign-up')
async def sign_up(request: Request):
    ...

@auth.get('/auth/sign-up')
async def sign_up(request: Request):
    ...
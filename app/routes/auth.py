from fastapi import Response, APIRouter

auth = APIRouter()

@auth.get('/auth')
async def auth():
    ...

@auth.get('/sign-up')
async def sign_up_page():
    ...

@auth.post('/sign-up')
async def sign_up():
    ...

@auth.get('/login')
async def login_page():
    ...

@auth.post('/login')
async def login():
    ...
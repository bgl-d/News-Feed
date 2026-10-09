from fastapi import Response, APIRouter

auth = APIRouter()

@auth.put('/login')
async def login():
    ...

@auth.get('/logout')
async def logout(response: Response):
    ...

@auth.put('/sign-up')
async def sign_up():
    ...
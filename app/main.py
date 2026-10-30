from fastapi import FastAPI
import uvicorn
from routes.feed import feed
from routes.auth import auth

app = FastAPI()
app.include_router(feed)
app.include_router(auth)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=5001, reload=True)
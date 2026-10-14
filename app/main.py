from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from routes.feed import feed

app = FastAPI()
app.include_router(feed)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=5001, reload=True)
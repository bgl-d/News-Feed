from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

# Setup for Jinja2 templates
templates = Jinja2Templates(directory='templates')
app.mount('/static', StaticFiles(directory='static'), name='static')
app.mount("/media", StaticFiles(directory="media"), name="media")

@app.get('/')
def home(request: Request):
    return templates.TemplateResponse(
        name='feed.html',
        request=request
    )

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=5001, reload=True)
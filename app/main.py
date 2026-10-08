from fastapi import FastAPI, requests
import uvicorn

app = FastAPI()

@app.get('/')
def news_feed():
    return('News Feed Page')

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=5001, reload=True)
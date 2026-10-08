from sqlalchemy.orm import Session

def create_post(db: Session, text: str, media: object):
    # task = feed.CreatePost()
    # post_id = hash(user_id + timestamp)
    # return task
    ...

def get_news_feed():
    # return db[Session]
    ...

def delete_post(post_id):
    # db.pop(post_id)
    ...
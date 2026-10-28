# from sqlalchemy import create_engine
# from sqlalchemy.orm import Session, sessionmaker
# from dependencies import Post, get_connection, Base


# def create_post(session: Session, author_handle:str, title:str, text_content:str, media_storage_link: str, ):
#     post = Post(author_handle=author_handle, title=title, text_content=text_content, media_storage_key=media_storage_link)
#     return post

# def get_post(db: Session, post_id: int):
#     ...

# def delete_post(db: Session, post_id: int):
#     ...
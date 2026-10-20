# from sqlalchemy.orm import Session
# from dependencies import Post


# def create_post(db: Session, author_handle:str, title:str, text_content:str, media_storage_link: str, ):
#     post = Post(author_handle=author_handle, title=title, text_content=text_content, media_storage_key=media_storage_link)
#     db.add(post)
#     db.commit()
#     db.refresh(post)
#     return post

# def get_post(db: Session, post_id: int):
#     ...

# def delete_post(db: Session, post_id: int):
#     ...
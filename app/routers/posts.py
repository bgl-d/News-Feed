from fastapi import APIRouter

router = APIRouter()


@router.get("/posts")
def get_posts():
    ...


@router.post("/posts")
def create_post():
    ...


@router.get("/posts/{post_id}")
def get_post(post_id: int):
    ...


@router.patch("/posts/{post_id}")
def update_post(post_id: int):
    ...


@router.delete("/posts/{post_id}")
def delete_post(post_id: int):
    ...

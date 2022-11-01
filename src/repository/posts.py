from sqlalchemy.orm import Session
from src.models import Post, Author


async def get_posts(db: Session):
    posts = db.query(Post).all()
    return posts


async def find_post_by_id(db: Session, post_id: int):
    post = {}

    return post


async def create_post(db: Session, post: dict):
    pass


async def update_post(db: Session, post_id: int, post: dict):
    pass


async def delete_post(db: Session, post_id: int):
    pass

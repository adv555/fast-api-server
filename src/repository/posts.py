from sqlalchemy.orm import Session
from src.models import Post, Author
from src.schemas.posts import UpdatePost, CreatePost, CreateAuthor


async def get_posts(db: Session, skip: int, limit: int):
    posts = db.query(Post).offset(skip).limit(limit).all()
    return {"posts": posts}


async def find_post_by_id(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    return post


async def create_post(db: Session, post: CreatePost):
    author = await create_author(db, post.author)
    new_post = Post(title=post.title, content=post.content, date=post.date, img_url=post.img_url)
    new_post.author = [author]
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


async def update_post(db: Session, post_id: int, post: UpdatePost):
    updated_post = db.query(Post).filter(Post.id == post_id).first()
    if updated_post:
        if post.title:
            updated_post.title = post.title
        if post.content:
            updated_post.content = post.content
        if post.img_url:
            updated_post.img_url = post.img_url

        db.commit()
        db.refresh(updated_post)

    return updated_post


async def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()

    return post


async def create_author(db: Session, author_name: str):
    author = db.query(Author).filter(Author.name == author_name).first()
    if not author:
        author = Author(name=author.name)
        db.add(author)
        db.commit()
        db.refresh(author)
    return author







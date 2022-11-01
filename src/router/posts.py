from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from db.connect import get_db
from src.repository.posts import get_posts, find_post_by_id, create_post, update_post, delete_post

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/")
async def get_all_posts(db: Session = Depends(get_db)):
    posts = await get_posts(db)
    return {"msg": "This is news", "posts": posts}


@router.get("/{post_id}")
async def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
    post = await find_post_by_id(db, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"News {post_id} not found",
        )
    return {"post": post_id}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_new_post(post: dict, db: Session = Depends(get_db)):
    new_post = await create_post(db, post)
    return {"msg": "News created", "post": new_post}


@router.put("/{post_id}")
async def update_post_by_id(post_id: int, post: dict, db: Session = Depends(get_db)):
    updated_post = await update_post(db, post_id, post)
    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"News {post_id} not found",
        )
    return {"msg": "News updated", "post": updated_post}


@router.delete("/{post_id}")
async def delete_post_by_id(post_id: int, db: Session = Depends(get_db)):
    post = await delete_post(db, post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"News {update_post} not found",
        )
    return {"msg": "News deleted", "post": post}

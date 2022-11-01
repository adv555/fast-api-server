from fastapi import APIRouter, Depends, HTTPException, status

from src.repository.posts import get_posts, find_post_by_id, create_post, update_post, delete_post

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/")
async def read_posts():
    posts = await get_posts()
    return {"msg": "This is news", "posts": posts}


@router.get("/{post_id}")
async def read_post_by_id(post_id: int):
    post = await find_post_by_id(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"News {post_id} not found",
        )
    return {"post": post_id}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_post(post: dict):
    new_post = await create_post(post)
    return {"msg": "News created", "post": new_post}


@router.put("/{post_id}")
async def update_post(post_id: int, post: dict):
    post = await update_post(post_id, post)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"News {post_id} not found",
        )
    return {"msg": "News updated", "post": post}


@router.delete("/{post_id}")
async def delete_post(post_id: int):
    post = await delete_post(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"News {update_post} not found",
        )
    return {"msg": "News deleted", "post": post}

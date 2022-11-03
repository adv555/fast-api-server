from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Author(BaseModel):
    id: int
    name: str = Field(max_length=50)
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True


class CreateAuthor(BaseModel):
    name: str = Field(max_length=50)


class Post(BaseModel):
    id: int
    img_url: str
    title: str
    content: str
    date: str
    created: datetime

    class Config:
        orm_mode = True


class PostList(BaseModel):
    posts: list[Post]


class CreatePost(BaseModel):
    img_url: str = Field(max_length=250, nullable=True, default=None)
    title: str = Field(max_length=150)
    content: str
    date: str
    author: str

    class Config:
        schema_extra = {
            "example": {
                "img_url": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
                "title": "My first post",
                "content": "This is my first post",
                "date": "2021-09-01",
                "author": "John Doe"
            }
        }



class UpdatePost(BaseModel):
    img_url: Optional[str] = None
    title: Optional[str] = Field(max_length=150)
    content: Optional[str] = Field(max_length=2000)
    date: Optional[str] = Field(max_length=50)

# class PostResponse(Post):
#     id: int
#     created: datetime
#
#     class Config:
#         orm_mode = True
#

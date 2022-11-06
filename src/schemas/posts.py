from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Author(BaseModel):
    id: int
    name: str
    created_at: datetime

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
    content: str = Field(max_length=2000)
    date: str = Field(max_length=50)
    author: str = Field(max_length=50)

    # def __getitem__(self, item):
    #     return getattr(self, item)

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
    img_url: Optional[str]
    title: Optional[str]
    content: Optional[str]



    class Config:
        schema_extra = {
            "example": {
                "img_url": "https://www.gravatar.com/avatar/205e460b479e2e5b48aec07710c08d50",
                "title": "My updated title",
                "content": "This is my updated post",

            }
        }

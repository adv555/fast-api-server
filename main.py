from typing import Union

from fastapi import FastAPI

from src.router import posts

app = FastAPI()

app.include_router(posts.router)


@app.get("/")
def read_root():
    return {"Hello": "Sasha"}





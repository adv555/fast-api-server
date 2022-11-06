from fastapi import FastAPI
from db.connect import SQLALCHEMY_DATABASE_URL
from src.repository.posts import save_post_to_db
from src.router import posts
from fastapi_utils.tasks import repeat_every
from fastapi_utils.session import FastAPISessionMaker
from src.utils.parse_data import parse_data

app = FastAPI()

sessionmaker = FastAPISessionMaker(SQLALCHEMY_DATABASE_URL)

app.include_router(posts.router)


@app.on_event("startup")
# @repeat_every(seconds=60 * 60 * 24)
async def parse_posts():
    print("Updating posts...")
    news = parse_data()
    for post in news:
        with sessionmaker.context_session() as db:
            await save_post_to_db(db, post)


@app.get("/")
def read_root():
    return {"Hello": "Sasha"}

# @app.post("/fetch_posts")
# async def fetch_posts(post: dict, db: Session = Depends(get_db)):
#     return save_post(db, post)

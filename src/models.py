from datetime import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

from db.connect import Base

news_author = Table(
    "news_author",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("post.id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("author.id"), primary_key=True),
)


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    img_url = Column(String(250), nullable=True)
    title = Column(String(150), nullable=False, unique=True)
    content = Column(String(2000), nullable=False)
    date = Column(String(50))
    created = Column(DateTime, default=datetime.now())
    author = relationship("Author", secondary=news_author, back_populates="post")
    # user = Column('user_id', ForeignKey('users.id', ondelete="CASCADE"), default=None)


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now())
    post = relationship("Post", secondary=news_author, back_populates="author")

# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     username = Column(String(150), nullable=False)
#     email = Column(String(150), nullable=False, unique=True)
#     password = Column(String(255), nullable=False)
#     avatar = Column(String(255))

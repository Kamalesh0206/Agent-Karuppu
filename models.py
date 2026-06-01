# database/models.py

from sqlalchemy import *

metadata = MetaData()

accounts = Table(
    "accounts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("access_token", Text),
    Column("status", String)
)

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("media_path", Text),
    Column("caption", Text),
    Column("hashtags", Text)
)
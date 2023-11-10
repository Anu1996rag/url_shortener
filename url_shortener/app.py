import secrets
import string
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import schemas, models, database
from .database import get_db

# create database
models.base.metadata.create_all(database.engine)


app = FastAPI()

chars = string.ascii_letters


@app.get("/")
def home():
    return "welcome to URL shortener API"


@app.post("/url")
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))

    db_url = models.URL(target_url=url.target_url,
                        key=key,
                        secret_key=secret_key)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

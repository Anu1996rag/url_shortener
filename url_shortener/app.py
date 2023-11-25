import validators
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import schemas, models, database, crud
from .database import get_db

# create database
models.base.metadata.create_all(database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return "welcome to URL shortener API"


@app.post("/url", response_model=schemas.ResponseModel)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Please enter a valid URL")

    db_url = crud.create_db_url(db, url)
    db_url.url = db_url.key
    return db_url


@app.get("/{url_key}")
def forward_to_target_url(url_key: str, db: Session = Depends(get_db)):
    db_url = crud.get_db_url_by_key(db, url_key)
    if db_url:
        return RedirectResponse(url=db_url.target_url, status_code=303)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Request URL not found or the key is invalid")

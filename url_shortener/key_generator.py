import secrets
import string
from sqlalchemy.orm import Session

from . import crud


chars = string.ascii_letters + string.digits


def create_random_key(length: int = 5) -> str:
    return "".join(secrets.choice(chars) for _ in range(length))


def create_unique_random_key(db: Session) -> str:
    key_generated = create_random_key()
    while crud.get_db_url_by_key(db, key_generated):
        key_generated = create_random_key()
    return key_generated


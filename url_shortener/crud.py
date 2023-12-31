from sqlalchemy.orm import Session

from . import schemas, models, key_generator


def create_db_url(db: Session, url: schemas.URLBase) -> models.URL:
    key = key_generator.create_unique_random_key(db)
    secret_key = f"{key}_{key_generator.create_random_key(length=8)}"

    db_url = models.URL(target_url=url.target_url,
                        key=key,
                        secret_key=secret_key)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def get_db_url_by_key(db: Session, url_key: str) -> models.URL | None:
    return (
        db.query(models.URL).filter(models.URL.key == url_key, models.URL.is_active).first()
    )


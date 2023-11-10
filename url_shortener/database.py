from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import DATABASE_URL

# create an engine first
engine = create_engine(DATABASE_URL)

# create a session
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative base class
base = declarative_base()


# database connection
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


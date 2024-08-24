from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "postgresql://rushi:pEHigGM2MImdT9YOrvKBSeBxG0P2Qo8b@dpg-cr4qhdo8fa8c73a63nlg-a.oregon-postgres.render.com/scrapingdata"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

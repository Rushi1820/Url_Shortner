from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "postgresql://scrapingdatabase_user:P7dMq2qFg3t0pVrDUVWgWL30liTi9IET@dpg-cqgt4p2ju9rs73ebui8g-a.singapore-postgres.render.com/scrapingdatabase"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

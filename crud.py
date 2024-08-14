from sqlalchemy.orm import Session
import models, schemas
import hashlib

def create_short_url(db: Session, url: schemas.URLCreate):
    short_code = hashlib.md5(url.original_url.encode()).hexdigest()[:6]
    db_url = models.URL(original_url=url.original_url, short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_short_code(db: Session, short_code: str):
    return db.query(models.URL).filter(models.URL.short_code == short_code).first()


def get_allurls_and_shortcode(db: Session):
    return db.query(models.URL).all()

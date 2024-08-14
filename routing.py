from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
import schemas, crud
from typing import List
from database import get_db

router = APIRouter()


@router.post("/shorten", response_model=schemas.URLResponse)
def create_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    db_url = crud.create_short_url(db, url)
    return db_url

@router.get("/redirect/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_short_code(db, short_code)
    if db_url:
      return RedirectResponse(url=db_url.original_url)
    else:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
 
    

@router.get("/getallurlsdetails", response_model=List[schemas.URLResponse])
def getalldetails(db: Session = Depends(get_db)):
    try:
        db_url = crud.get_allurls_and_shortcode(db)
        return db_url
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


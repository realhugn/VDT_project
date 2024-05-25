from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import user_handler, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return user_handler.create_user(db=db, user=user)
from sqlalchemy.orm import Session
import model, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = model.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

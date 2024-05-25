from sqlalchemy.orm import Session
import model, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = model.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 50):
    return db.query(model.User).offset(skip).limit(limit).all()
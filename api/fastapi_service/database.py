from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:123@localhost:5434/pythondb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import FastAPI
from database import engine
from model import Base
from route import users
from fastapi.middleware.cors import CORSMiddleware


# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the users router
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

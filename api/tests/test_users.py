from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app
from database import Base, get_db

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "John Doe", "gender": "male", "university": "MIT", "phone": "1234567890"})
    assert response.status_code == 200
    data = response.json()
    id = data["id"]
    assert data["name"] == "John Doe"
    assert data["gender"] == "male"
    assert data["university"] == "MIT"
    assert data["phone"] == "1234567890"

    client.delete(f"/users{id}")

def test_create_user_fail_missing_field():
    # test
    response = client.post("/users/", json={"name": "John Doe", "gender": "male", "university": "MIT"})
    assert response.status_code == 422

def test_read_user():
    user = client.post("/users/", json={"name": "John Doe", "gender": "male", "university": "MIT", "phone": "1234567890"}).json()
    id = user["id"]
    response = client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["gender"] == "male"
    assert data["university"] == "MIT"
    assert data["phone"] == "1234567890"

    client.delete(f"/users{id}")

def test_read_not_found():
    response = client.get("/users/1123213241414")
    assert response.status_code == 404

def test_update_user():
    # create a new user
    user = client.post("/users/", json={"name": "John Doe", "gender": "male", "university": "MIT", "phone": "1234567890"}).json()
    id = user["id"]
    response = client.put(f"/users/{id}", json={"name": "Jane Doe", "gender": "female", "university": "Harvard", "phone": "0987654321"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane Doe"
    assert data["gender"] == "female"
    assert data["university"] == "Harvard"
    assert data["phone"] == "0987654321"

    #clean 
    client.delete(f"/users{id}")

def test_update_user_fail_missing_field():
    # test
    user = client.post("/users/", json={"name": "John Doe", "gender": "male", "university": "MIT", "phone": "1234567890"}).json()
    id = user["id"]
    response = client.put(f"/users/{id}", json={"name": "John Doe", "gender": "male", "university": "MIT"})
    assert response.status_code == 422

    #clean 
    client.delete(f"/users{id}")
    
def test_delete_user():
    user = client.post("/users/", json={"name": "John Doe", "gender": "male", "university": "MIT", "phone": "1234567890"}).json()
    id = user["id"]
    response = client.delete(f"/users/{id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"

    response = client.get(f"/users/{id}")
    assert response.status_code == 404
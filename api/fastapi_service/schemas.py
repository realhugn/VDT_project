from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    gender: str
    university: str
    phone: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class ConfigDict:
        from_attributes = True

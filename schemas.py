from pydantic import BaseModel
from typing import Optional

class AdminCreate(BaseModel):
    username: str
    email: str
    password: str

class Admin(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    identity_document: str
    rut: str

class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    identity_document: str
    rut: str

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: int

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: int

    class Config:
        orm_mode = True

class Transaction(BaseModel):
    id: int
    amount: float
    user_id: int
    product_id: int

class TransactionCreate(BaseModel):
    product_id: int

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class AdminLogin(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
import auth, models
from database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Obtener el admin actual
def get_current_admin(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return auth.get_current_admin(db, token)

# Obtener el user actual
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    return auth.get_current_user(db, token)

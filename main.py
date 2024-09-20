from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
import models
import schemas
import crud
import auth
from database import SessionLocal, engine  # Cambiado a importación absoluta
from dependencies import get_current_user, get_current_admin  # Cambiado a importación absoluta


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear un token para Admin o User (Login)
@app.post("/token", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Comprobar si es Admin o User
    admin = auth.authenticate_admin(db, form_data.username, form_data.password)
    if admin:
        access_token = auth.create_access_token(data={"sub": admin.username, "role": "admin"})
        return {"access_token": access_token, "token_type": "bearer"}

    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if user:
        access_token = auth.create_access_token(data={"sub": user.username, "role": "user"})
        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

# Rutas para la creación de usuarios y administradores
@app.post("/admin/", response_model=schemas.Admin)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    return crud.create_admin(db=db, admin=admin)

@app.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Ruta para que los admins añadan productos (sólo accesible para admins)
@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db), current_admin: schemas.Admin = Depends(get_current_admin)):
    return crud.create_product(db=db, product=product)

# Ruta para que todos puedan ver los productos (accesible para users y admins)
@app.get("/products/", response_model=list[schemas.Product])
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db=db)

# Ruta para que los usuarios puedan realizar compras (sólo accesible para usuarios)
@app.post("/transactions/", response_model=schemas.Transaction)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return crud.create_transaction(db=db, transaction=transaction, user_id=current_user.id)

# Ruta para que los admins aprueben o rechacen transacciones (sólo accesible para admins)
@app.post("/transactions/approve")
def approve_transaction(transaction_id: int, approved: bool, db: Session = Depends(get_db), current_admin: schemas.Admin = Depends(get_current_admin)):
    return crud.approve_transaction(db=db, transaction_id=transaction_id, approved=approved)

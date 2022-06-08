from datetime import timedelta
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
from user import schemas
from user.auth import create_access_token, authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, pwd_context
from user.schemas import Token
import models

router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "authorized": "true"}


@router.post('/auth')
async def users(user: schemas.User, db: Session = Depends(get_db)):
    user.password = pwd_context.hash(user.password)
    if db.query(models.Users).filter_by(username=user.username).first():
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail='Username is already exist'
        )
    new_users = models.Users(**user.dict())
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    return {
        "authorized": 'True',
        "token": new_users.password
    }

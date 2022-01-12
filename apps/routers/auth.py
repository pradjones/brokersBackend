from typing import Any, List
from fastapi import APIRouter, Body, APIRouter, Query, HTTPException, Request, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import json 

from apps.crud import user
from apps.schemas.user import UserInDBBase, UserUpdate, UserCreate, User
from apps.core.auth import authenticate, create_access_token
import dependencies as deps

router = APIRouter()

@router.post("/signup", status_code=201)
def create_user_signup(*, db: Session = Depends(deps.get_db), user_in: UserCreate) -> Any:
    # Check if user with the email already exists
    if user.get_by_email(db=db, email=user_in.email):
        raise HTTPException(status_code=400, detail=f"User with this email already exists")

    new_user = user.create(db=db, obj_in=user_in)
    return new_user

@router.post("/login")
def login(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    # Get the JWT for a user with data from OAuth2 request form body 
    login_user = authenticate(email=form_data.username, password=form_data.password, db=db)
    if not login_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {
        "access_token": create_access_token(sub=login_user.id),
        "token_type": "bearer",
    }

@router.get("/me", response_model=User)
def read_users_me(current_user: User = Depends(deps.get_current_user)):
    # fetch the current logged in user

    user = current_user
    return user
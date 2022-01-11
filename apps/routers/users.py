from typing import Any, List
from fastapi import APIRouter, Body, APIRouter, Query, HTTPException, Request, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import json 

from apps.crud import user
from apps.schemas.user import UserInDBBase, UserUpdate, UserCreate
import dependencies as deps

router = APIRouter()


@router.get("/users", status_code=200, response_description="List Users")
def list_users(db: Session = Depends(deps.get_db)) -> List[UserInDBBase]:
    """
    GET ALL USERS
    """
    users = user.get_multi(db=db, limit=10)
    return users

@router.get("/users/{user_id}", status_code=200, response_description="Get User Details")
def get_user(*, user_id: int, db: Session = Depends(deps.get_db)) -> Any:
    user_info = user.get(db=db, id=user_id)

    if not user_info:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} was not found")
    
    return user_info

@router.put("/users/{user_id}", response_description="Update user details")
def update_user(*, user_id: int, db: Session = Depends(deps.get_db), user_in: UserUpdate = Body(...)):
    user_in = jsonable_encoder(user_in)
    if len(user_in) >= 1:
        curr_user = user.get(db=db, id=user_id)
        if not curr_user:
            raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")

        updated_user = user.update(db=db, db_obj=curr_user,obj_in=user_in)
        return updated_user
    
    raise HTTPException(status_code=400, detail=f"Invalid user information")

@router.post("/users/", response_description="New user details")
def create_user(*, db: Session = Depends(deps.get_db), user_in: UserCreate = Body(...)):
    # check validity of user_in
    if user.get_by_email(db=db, email=user_in.email):
        return f"User with this email already exists"

    new_user = user.create(db=db, obj_in=user_in)
    return new_user

@router.delete("/users/{user.id}", response_description="Deleted user information")
def remove_user(*, user_id: int, db: Session = Depends(deps.get_db)):
    user_info = user.get(db=db, id=user_id)
    # Check user with the given id exists
    if user_info:
        user.remove(db=db, id=user_id)
    else: 
        return f"User with id {user_id} not found"
    
    return user_info


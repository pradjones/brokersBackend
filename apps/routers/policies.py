from typing import Any, List
from fastapi import APIRouter, Body, HTTPException, Request, Depends 
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import json

from apps.crud import policies
from apps.schemas.policies import PoliciesInDBBase, PoliciesCreate, PoliciesUpdate

import dependencies as deps 

router = APIRouter()

@router.get("/policies", status_code=200, response_description="List policies")
def list_policies(db: Session = Depends(deps.get_db)) -> List[PoliciesInDBBase]:
    all_policies = policies.get_multi(db=db, limit=10)
    return all_policies

@router.get("/policies/{policies_id}", status_code=200, response_description="Get policy details")
def get_policy(*, policies_id: int, db: Session = Depends(deps.get_db)) -> Any:
    policies_info = policies.get(db=db, id=policies_id)

    if not policies_info:
        raise HTTPException(status_code=404, detail=f"Policy with id {policies_id} not found")

    return policies_info

@router.put("/policies/{policies_id}", response_description="Update policy details")
def update_policy(*, policies_id: int, db: Session = Depends(deps.get_db), policies_in: PoliciesUpdate = Body(...)):
    policies_in = jsonable_encoder(policies_in)
    if len(policies_in) >= 1:
        curr_policy = policies.get(db=db, id=policies_id)
        if not curr_policy:
            raise HTTPException(status_code=404, detail=f"Policy with id {policies_id} not found")

        # Prevent unchanged values from becoming null
        for key in policies_in:
            if policies_in[key] is None:
                policies_in[key] = getattr(curr_policy, key)
  
        updated_policy = policies.update(db=db, db_obj=curr_policy, obj_in=policies_in)
        return updated_policy

    raise HTTPException(status_code=400, detail=f"Invalid policy information")

@router.post("/policies", response_description="New policy details")
def create_policy(*, db: Session = Depends(deps.get_db), policies_in: PoliciesCreate = Body(...)):
    if policies.get_policy_name(db=db, policy_name=policies_in.policyName):
        if policies.get_insurer_company(db=db, insurer_company=policies_in.insurerCompany):
            if policies.get_policy_version(db=db,policy_version=policies_in.policyVersion):
                return f"Policy with these details already exists"

    new_policy = policies.create(db=db, obj_in=policies_in)
    return new_policy

@router.delete("/policies/{policies_id}", response_description="Deleted policy information")
def remove_policy(*, policies_id: int, db: Session = Depends(deps.get_db)):
    policies_info = policies.get(db=db, id=policies_id)

    if policies_info:
        policies.remove(db=db, id=policies_id)
    else:
        return f"Policy with id {policies_id} not found"
    
    return policies_info
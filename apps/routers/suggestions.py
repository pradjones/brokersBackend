from typing import Any, List
from fastapi import APIRouter, Body, HTTPException, Request, Depends 
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import json

from apps.crud import suggestions
from apps.schemas.suggestions import SuggestionsInDBBase, SuggestionsCreate, SuggestionsUpdate

import dependencies as deps

router = APIRouter()

@router.get("/suggestions", status_code=200, response_description="List suggestions")
def list_suggestions(db: Session = Depends(deps.get_db)) -> List[SuggestionsInDBBase]:
    all_suggestions = suggestions.get_multi(db=db, limit=10)
    return all_suggestions

@router.get("/suggestions/{suggestions_id}", status_code=200, response_description="Get suggestion details")
def get_suggestion(*, suggestions_id: int, db: Session = Depends(deps.get_db)) -> Any:
    suggestion_info = suggestions.get(db=db, id=suggestions_id)

    if not suggestion_info:
        raise HTTPException(status_code=404, detail=f"Suggestion with ID {suggestions_id} not found")

    return suggestion_info

@router.put("/suggestions/{suggestions_id}", response_description="Update suggestion details")
def update_suggestion(*, suggestions_id: int, db: Session = Depends(deps.get_db), suggestions_in: SuggestionsUpdate = Body(...)):
    suggestions_in = jsonable_encoder(suggestions_in)
    if len(suggestions_in) >= 1:
        curr_suggestion = suggestions.get(db=db, id=suggestions_id)
        if not curr_suggestion:
            raise HTTPException(status_code=404, detail=f"Suggestion with id {suggestions_id} not found")

        # Prevent unchanged values from becoming null
        for key in suggestions_in:
            if suggestions_in[key] is None:
                suggestions_in[key] = getattr(curr_suggestion, key)

        updated_suggestion = suggestions.update(db=db, db_obj=curr_suggestion, obj_in=suggestions_in)
        return updated_suggestion

    raise HTTPException(status_code=400, detail=f"Invalid suggestions information")

@router.post("/suggestions", response_description="New suggestion details")
def create_suggestion(*, db: Session = Depends(deps.get_db), suggestions_in: SuggestionsCreate = Body(...)):
    if suggestions.get_by_client_organisation(db=db, client_organisation=suggestions_in.clientOrganisation):
        if suggestions.get_by_policy_type(db=db, policy_type=suggestions_in.policyType):
            return f"Suggestion with these details already exists"

    new_suggestion = suggestions.create(db=db, obj_in=suggestions_in)
    return new_suggestion

@router.delete("/suggestions/{suggestions_id}", response_description="Deleted suggestions information")
def remove_suggestion(*, suggestions_id: int, db: Session = Depends(deps.get_db)):
    suggestions_info = suggestions.get(db=db, id=suggestions_id)

    # check if a suggestion with the given id exists 
    if suggestions_info:
        suggestions.remove(db=db, id=suggestions_id)
    else:
        return f"Suggestion with id {suggestions_id} not found"

    return suggestions_info
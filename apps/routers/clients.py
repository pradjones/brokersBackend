from typing import Any, List
from fastapi import APIRouter, Body, Query, HTTPException, Request, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import json 

from apps.crud import clients 
from apps.schemas.clients import ClientsInDBBase, ClientsUpdate, ClientsCreate 
import dependencies as deps 

router = APIRouter() 

@router.get("/clients", status_code=200, response_description="List all clients")
def list_clients(db: Session = Depends(deps.get_db)) -> List[ClientsInDBBase]:
    all_clients = clients.get_multi(db=db, limit=10)
    return all_clients

@router.get("/clients/{clients_id}", status_code=200, response_description="Get client details")
def get_client(*, clients_id: int, db: Session = Depends(deps.get_db)) -> Any:
    client_info = clients.get(db=db, id=clients_id)

    if not client_info:
        raise HTTPException(status_code=404, detail=f"Client with id {clients_id} was not found")

    return client_info

@router.put("/clients/{clients_id}", status_code=200, response_description="Update client details")
def update_client(*, clients_id: int, db: Session = Depends(deps.get_db), client_in: ClientsUpdate = Body(...)):
    clients_in = jsonable_encoder(client_in)
    if len(clients_in) >= 1:
        curr_client = clients.get(db=db, id=clients_id)
        if not curr_client:
            raise HTTPException(status_code=404, detail=f"Client with id {clients_id} not found")

        # Prevent unchanged values from becoming null
        for key in clients_in:
            if clients_in[key] is None:
                clients_in[key] = getattr(curr_client, key)

        updated_client = clients.update(db=db, db_obj=curr_client, obj_in=clients_in)
        return updated_client
    
    raise HTTPException(status_code=400, detail=f"Invalid client information")

@router.post("/clients", response_description="New client details")
def create_client(*, db: Session = Depends(deps.get_db), clients_in: ClientsCreate = Body(...)):
    if clients.get_client_name(db=db, client_name=clients_in.clientName):
        return f"Client with these details already exist"

    new_client = clients.create(db=db, obj_in=clients_in)
    return new_client

@router.delete("/clients/{clients_id}", response_description="Deleted client information")
def remove_client(*, clients_id: int, db: Session = Depends(deps.get_db)):
    clients_info = clients.get(db=db, id=clients_id)

    if clients_info:
        clients.remove(db=db, id=clients_id)
    else:
        return f"Client with id {clients_id} not found"

    return clients_info
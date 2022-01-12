from typing import Any, List 
from fastapi import APIRouter, Body, HTTPException, Request, Depends 
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session 
import json 

from apps.crud import agents 
from apps.schemas.agents import AgentsInDBBase, AgentsUpdate, AgentsCreate

import dependencies as deps 

router = APIRouter()

@router.get("/agents", status_code=200, response_description="List agents")
def list_agents(db: Session = Depends(deps.get_db)) -> List[AgentsInDBBase]:
    all_agents = agents.get_multi(db=db, limit=10)
    return all_agents

@router.get("/agents/{agents_id}", status_code=200, response_description="Get agent details")
def get_agent(*, agents_id: int, db: Session = Depends(deps.get_db)) -> Any:
    agent_info = agents.get(db=db, id=agents_id)
    
    if not agent_info:
        raise HTTPException(status_code=404, detail=f"Agent with id {agents_id} not found")

    return agent_info

@router.put("/agents/{agents_id}", response_description="Update agent details")
def update_agent(*, agents_id: int, db: Session = Depends(deps.get_db), agents_in: AgentsUpdate = Body(...)):
    agents_in = jsonable_encoder(agents_in)
    if len(agents_in) >= 1:
        curr_agent = agents.get(db=db, id=agents_id)
        if not curr_agent:
            raise HTTPException(status_code=404, detail=f"Agent with id {agents_id} not found")

        # Prevent unchanged values from becoming null
        for key in agents_in:
            if agents_in[key] is None:
                agents_in[key] = getattr(curr_agent, key)

        updated_agent = agents.update(db=db, db_obj=curr_agent, obj_in=agents_in)
        return updated_agent

    raise HTTPException(status_code=400, detail=f"Invalid agent information")

@router.post("/agents", response_description="New agent details")
def create_agent(*, db: Session = Depends(deps.get_db), agents_in: AgentsCreate = Body(...)):
    if agents.get_agent_name(db=db, agent_name=agents_in.agentName):
        return f"Agent with these details already exist"

    new_agent = agents.create(db=db, obj_in=agents_in)
    return new_agent

@router.delete("/agents/{agents.id}", response_description="Deleted agent information")
def remove_agent(*, agents_id: int, db: Session = Depends(deps.get_db)):
    agents_info = agents.get(db=db, id=agents_id)

    if agents_info:
        agents.remove(db=db, id=agents_id)
    else:
        return f"Agent with id {agents_id} not found"

    return agents_info
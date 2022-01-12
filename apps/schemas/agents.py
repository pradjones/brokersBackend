from typing import Optional 
from pydantic import BaseModel
from datetime import datetime 

class AgentsBase(BaseModel):
    agentName: Optional[str] = None
    position: Optional[str] 
    managerId: Optional[int] 
    joinDate: Optional[datetime]

class AgentsCreate(AgentsBase):
    agentName: str

class AgentsUpdate(AgentsBase):
    pass

class AgentsInDBBase(AgentsBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Agents(AgentsInDBBase):
    pass

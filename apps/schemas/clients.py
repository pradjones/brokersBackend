from typing import Optional 
from pydantic import BaseModel

class ClientsBase(BaseModel):
    clientName: Optional[str] = None
    serviceOffering: Optional[str]
    clientAddress: Optional[str]
    region: Optional[str]

class ClientsCreate(ClientsBase):
    clientName: str 

class ClientsUpdate(ClientsBase):
    pass

class ClientsInDBBase(ClientsBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Clients(ClientsInDBBase):
    pass
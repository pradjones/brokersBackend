from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class SalesBase(BaseModel):
    quoteAmount: Optional[float] = None 
    conversionDate: Optional[datetime]
    quotationDate: Optional[datetime] = None 
    expiryDate: Optional[datetime]
    flag: Optional[bool]
    policyId: Optional[int]
    agentId: Optional[int] = None
    clientId: Optional[int] = None

class SalesCreate(SalesBase):
    quoteAmount: float
    clientId: int
    agentId: int
    quotationDate: datetime

class SalesUpdate(SalesBase):
    pass

class SalesInDBBase(SalesBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Sales(SalesInDBBase):
    pass
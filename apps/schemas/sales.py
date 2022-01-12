from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class SalesBase(BaseModel):
    quoteAmount: Optional[float] = None 
    policyType: Optional[str]
    clientOrganisation: Optional[str] = None 
    agent: Optional[str] = None 
    conversionDate: Optional[datetime]
    quotationDate: Optional[datetime] = None 
    expiryDate: Optional[datetime]
    flag: Optional[bool]
    policyName: Optional[str]
    company: Optional[str]

class SalesCreate(SalesBase):
    quoteAmount: float
    clientOrganisation: str
    agent: str
    quotationDate: datetime

class SalesUpdate(SalesBase):
    pass

class SalesInDBBase(SalesBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Sales(SalesInDBBase):
    pass
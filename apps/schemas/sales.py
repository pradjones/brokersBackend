from typing import Optional
from pydantic import BaseModel
from datetime import date

class SalesBase(BaseModel):
    quoteAmount: Optional[float] = None 
    policyType: Optional[str]
    clientOrganisation: Optional[str] = None 
    agent: Optional[str] = None 
    conversionDate: Optional[date]
    quotationDate: Optional[date] = None 
    expiryDate: Optional[date]
    flag: Optional[bool]
    policyName: Optional[str]
    company: Optional[str]

class SalesCreate(SalesBase):
    quoteAmount: float
    clientOrganisation: str
    agent: str
    quotationDate: date

class SalesUpdate(SalesBase):
    pass

class SalesInDBBase(SalesBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Sales(SalesInDBBase):
    pass
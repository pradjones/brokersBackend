from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class PoliciesBase(BaseModel):
    policyType: Optional[str] 
    policyName: Optional[str] = None
    insurerCompany: Optional[str] = None
    policyAmount: Optional[float] 
    policyVersion: Optional[datetime] = None

class PoliciesCreate(PoliciesBase):
    policyName: str
    insurerCompany: str
    policyVersion: datetime

class PoliciesUpdate(PoliciesBase):
    pass

class PoliciesInDBBase(PoliciesBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Policies(PoliciesInDBBase):
    pass
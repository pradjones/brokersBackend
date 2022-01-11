from typing import Optional

from pydantic import BaseModel

class SuggestionsBase(BaseModel):
    clientOrganisation: Optional[str] = None
    suggestion: Optional[bool] 
    policyType: Optional[str] = None
    insurerCompany: Optional[str] 
    quoteAmount: Optional[float]

class SuggestionsCreate(SuggestionsBase):
    clientOrganisation: str
    policyType: str

class SuggestionsUpdate(SuggestionsBase):
    pass

class SuggestionsInDBBase(SuggestionsBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Suggestions(SuggestionsInDBBase):
    pass
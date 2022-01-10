from typing import DefaultDict, Optional
import uuid
from pydantic import BaseModel, Field


class PolicyModel(BaseModel):

    # id: str = Field(default_factory=uuid.uuid4, alias="_id")
    # name: str = Field(...)
    # completed: bool = False

    # class Config:
    #     allow_population_by_field_name = True
    #     scheme_extra = {
    #         "example": {
    #             "id": "001",
    #             "name": "Allianz Business Pack", 
    #             "completed": "Allianz Business Pack" 
    #         }
    #     }
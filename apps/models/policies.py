from sqlalchemy import String, Column, Boolean, Integer, Float, DateTime
from sqlalchemy.orm import relationship 

from apps.db.base_class import Base

class Policies(Base):
    id = Column(Integer, primary_key=True, index=True)
    policyType = Column(String(256), nullable=True)
    policyName = Column(String(256), nullable=False)
    insurerCompany = Column(String(256), nullable=False)
    policyAmount = Column(Float, nullable=True) 
    policyVersion = Column(DateTime, nullable=False)

    children = relationship("Sales")



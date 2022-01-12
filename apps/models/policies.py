from sqlalchemy import String, Column, Boolean, Integer, Float, DateTime
from sqlalchemy.orm import relationship 

from apps.db.base_class import Base

class Policies(Base):
    id = Column(Integer, primary_key=True, index=True)
    policyType = Column(String(256), nullable=True)
    policyName = Column(String(256), nullable=True)
    insurerCompany = Column(String(256), nullable=True)
    policyAmount = Column(Float, nullable=True)
    policyVersion = Column(DateTime, nullable=True)



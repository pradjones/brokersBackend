from sqlalchemy import String, Column, Boolean, Float, Integer, DateTime
from sqlalchemy.orm import relationship

from apps.db.base_class import Base

class Sales(Base):
    id = Column(Integer, primary_key=True, index=True)
    quoteAmount = Column(Float, nullable=False)
    policyType = Column(String(256), nullable=True)
    clientOrganisation = Column(String(256), nullable=False)
    agent = Column(String(256), nullable=True)
    conversionDate = Column(DateTime, nullable=True)
    quotationDate = Column(DateTime, nullable=False)
    expiryDate = Column(DateTime, nullable=True)
    flag = Column(Boolean, nullable=True)
    policyName = Column(String(256), nullable=True)
    company = Column(String(256), nullable=True)
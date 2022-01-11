from sqlalchemy import String, Column, Boolean, Float, Integer, Date
from sqlalchemy.orm import relationship

from apps.db.base_class import Base

class Sales(Base):
    id = Column(Integer, primary_key=True, index=True)
    quoteAmount = Column(Float, nullable=True)
    policyType = Column(String(256), nullable=True)
    clientOrganisation = Column(String(256), nullable=True)
    agent = Column(String(256), nullable=True)
    conversionDate = Column(Date, nullable=True)
    quotationDate = Column(Date, nullable=True)
    expiryDate = Column(Date, nullable=True)
    flag = Column(Boolean, nullable=True)
    policyName = Column(String(256), nullable=True)
    company = Column(String(256), nullable=True)
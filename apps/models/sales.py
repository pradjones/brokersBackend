from sqlalchemy import String, Column, Boolean, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from apps.db.base_class import Base

class Sales(Base):
    id = Column(Integer, primary_key=True, index=True)
    quoteAmount = Column(Float, nullable=False)
    conversionDate = Column(DateTime, nullable=True)
    quotationDate = Column(DateTime, nullable=False)
    expiryDate = Column(DateTime, nullable=True)
    flag = Column(Boolean, nullable=True)

    policyId = Column(Integer, ForeignKey("policies.id"))
    agentId = Column(Integer, ForeignKey("agents.id"))
    clientId = Column(Integer, ForeignKey("clients.id"))
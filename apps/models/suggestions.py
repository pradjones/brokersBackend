from sqlalchemy import String, Boolean, Column, Float, Integer
from sqlalchemy.orm import relationship

from apps.db.base_class import Base

class Suggestions(Base):
    id = Column(Integer, primary_key=True, index=True)
    clientOrganisation = Column(String(256), nullable=False)
    suggestion = Column(Boolean, default=False)
    policyType = Column(String(256), nullable=True)
    insurerCompany = Column(String(256), nullable=True)
    quoteAmount = Column(Float, nullable=True)

from sqlalchemy import String, Column, Boolean, Float, Integer 
from sqlalchemy.orm import relationship

from apps.db.base_class import Base 

class Clients(Base):
    id = Column(Integer, primary_key=True, index=True)
    clientName = Column(String(256), nullable=False)
    serviceOffering = Column(String(256), nullable=True)
    clientAddress = Column(String(256), nullable=True)
    region = Column(String(256), nullable=True)

    children = relationship("Sales")
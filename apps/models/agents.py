from sqlalchemy import String, Column, Integer, DateTime 
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null

from apps.db.base_class import Base 

class Agents(Base):
    id = Column(Integer, primary_key=True, index=True)
    agentName = Column(String(256), nullable=True)
    position = Column(String(256), nullable=True)
    managerId = Column(Integer, nullable=True)
    joinDate = Column(DateTime, nullable=True)
from typing import Any, Dict, Optional, Union
from datetime import datetime

from sqlalchemy.orm import Session

from apps.crud.base import CRUDBase
from apps.models.agents import Agents 
from apps.schemas.agents import AgentsCreate, AgentsUpdate

class CRUDAgents(CRUDBase[Agents, AgentsCreate, AgentsUpdate]):
    def update (
        self, db: Session, *, db_obj: Agents, obj_in: Union[AgentsUpdate, Dict[str, Any]]
    ) -> Agents:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_agent_name(self, db: Session, *, agent_name: str) -> Optional[Agents]:
        return db.query(Agents).filter(Agents.agentName == agent_name).first()

agents = CRUDAgents(Agents)
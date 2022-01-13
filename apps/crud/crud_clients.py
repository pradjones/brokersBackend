from typing import Optional, Union, Any, Dict

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update

from apps.crud.base import CRUDBase 
from apps.models.clients import Clients
from apps.schemas.clients import ClientsCreate, ClientsUpdate

class CRUDClients(CRUDBase[Clients, ClientsCreate, ClientsUpdate]):
    def update(
        self, db: Session, *, db_obj: Clients, obj_in: Union[ClientsUpdate, Dict[str, Any]]
    ) -> Clients:
        if isinstance(obj_in, dict):
            update_data = obj_in 
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_client_names(self, db: Session, *, client_name: str) -> Optional[Clients]:
        return db.query(Clients).filter(Clients.clientName == client_name).first()

clients = CRUDClients(Clients)
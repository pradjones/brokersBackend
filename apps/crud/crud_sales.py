from typing import Optional, Any, Dict, Union
import math
from datetime import date

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update

from apps.crud.base import CRUDBase
from apps.models.sales import Sales
from apps.schemas.sales import SalesCreate, SalesUpdate

def compare_float(a, b, tol):
    return abs(a-b) <= tol

class CRUDSales(CRUDBase[Sales, SalesCreate, SalesUpdate]):
    def update(
        self, db: Session, *, db_obj: Sales, obj_in: Union[SalesUpdate, Dict[str, Any]]
    ) -> Sales:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_by_quote_amount(self, db: Session, *, quote_amount: float) -> Optional[Sales]:
        # todo: change to correctly compare floating point values
        return db.query(Sales).filter(Sales.quoteAmount == quote_amount).first() 

    def get_by_client_organisation(self, db: Session, *, client_organisation: str) -> Optional[Sales]:
        return db.query(Sales).filter(Sales.clientOrganisation == client_organisation).first()

    def get_by_agent(self, db: Session, *, agent: str) -> Optional[Sales]:
        return db.query(Sales).filter(Sales.agent == agent).first()

    def get_by_quotation_date(self, db: Session, *, quotation_date: date) -> Optional[Sales]:
        return db.query(Sales).filter(Sales.quotationDate == quotation_date)

sales = CRUDSales(Sales)

from typing import Any, Dict, Optional, Union
from datetime import datetime

from sqlalchemy.orm import Session

from apps.crud.base import CRUDBase
from apps.models.policies import Policies
from apps.schemas.policies import PoliciesCreate, PoliciesUpdate

class CRUDPolicies(CRUDBase[Policies, PoliciesCreate, PoliciesUpdate]):
    def update(
        self, db: Session, *, db_obj: Policies, obj_in: Union[PoliciesUpdate, Dict[str, Any]]
    ) -> Policies:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)

        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_policy_name(self, db: Session, *, policy_name: str) -> Optional[Policies]:
        return db.query(Policies).filter(Policies.policyName == policy_name).first()

    def get_insurer_company(self, db: Session, *, insurer_company: str) -> Optional[Policies]:
        return db.query(Policies).filter(Policies.insurerCompany == insurer_company).first()

    def get_policy_version(self, db: Session, *, policy_version: datetime) -> Optional[Policies]:
        return db.query(Policies).filter(Policies.policyVersion == policy_version).first()

policies = CRUDPolicies(Policies)
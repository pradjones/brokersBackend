from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from apps.crud.base import CRUDBase
from apps.models.suggestions import Suggestions
from apps.routers.sales import update_sale
from apps.schemas.suggestions import SuggestionsCreate, SuggestionsUpdate

class CRUDSuggestions(CRUDBase[Suggestions, SuggestionsCreate, SuggestionsUpdate]):
    def update(
        self, db: Session, *, db_obj: Suggestions, obj_in: Union[SuggestionsUpdate, Dict[str, Any]]
    ) -> Suggestions:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        
        return super().update(db, db_obj=db_obj, obj_in=update_data)

    def get_by_client_organisation(self, db: Session, *, client_organisation: str) -> Optional[Suggestions]:
        return db.query(Suggestions).filter(Suggestions.clientOrganisation == client_organisation).first()

    def get_by_policy_type(self, db: Session, *, policy_type: str) -> Optional[Suggestions]:
        return db.query(Suggestions).filter(Suggestions.policyType == policy_type).first()

suggestions = CRUDSuggestions(Suggestions)
from typing import Any, List
from fastapi import APIRouter, Body, Query, HTTPException, Request, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import json

from apps.crud import sales
from apps.schemas.sales import SalesInDBBase, SalesUpdate, SalesCreate
import dependencies as deps

router = APIRouter()

@router.get("/sales", status_code=200, response_description="List all sales")
def list_sales(db: Session = Depends(deps.get_db)) -> List[SalesInDBBase]:
    all_sales = sales.get_multi(db=db)
    return all_sales

@router.get("/sales/{sales_id}", status_code=200, response_description="Get sale details")
def get_sale(*, sales_id: int, db: Session = Depends(deps.get_db)) -> Any:
    sale_info = sales.get(db=db, id=sales_id)

    if not sale_info:
        raise HTTPException(status_code=404, detail=f"Sale with ID {sales_id} was not found")

    return sale_info

@router.put("/sales/{sales_id}", status_code=200, response_description="Update sale details")
def update_sale(*, sales_id: int, db: Session = Depends(deps.get_db), sales_in: SalesUpdate = Body(...)):
    sales_in = jsonable_encoder(sales_in)
    if len(sales_in) >= 1:
        curr_sale = sales.get(db=db, id=sales_id)
        if not curr_sale:
            raise HTTPException(status_code=404, detail=f"Sale with id {sales_id} not found")

        # Prevent unchanged values from becoming null
        for key in sales_in:
            if sales_in[key] is None:
                sales_in[key] = getattr(curr_sale, key)

        updated_sale = sales.update(db=db, db_obj=curr_sale, obj_in=sales_in)
        return updated_sale
    
    raise HTTPException(status_code=400, detail=f"Invalid sales information")

@router.post("/sales", response_description="New sale details")
def create_sale(*, db: Session = Depends(deps.get_db), sales_in: SalesCreate = Body(...)):
    if sales.get_by_quote_amount(db=db, quote_amount=sales_in.quoteAmount):
        if sales.get_by_client_organisation(db=db, client_organisation=sales_in.clientOrganisation):
            if sales.get_by_agent(db=db, agent=sales_in.agent):
                if sales.get_by_quotation_date(db=db, quotation_date=sales_in.quotationDate):
                    return f"Sale with these details already exists"

    new_sale = sales.create(db=db, obj_in=sales_in)
    return new_sale

@router.delete("/sales/{sales_id}", response_description="Deleted sales information")
def remove_sale(*, sales_id: int, db: Session = Depends(deps.get_db)):
    sales_info = sales.get(db=db, id=sales_id)
    # check if a sale with the given id exists
    if sales_info:
        sales.remove(db=db, id=sales_id)
    else:
        return f"Sale with id {sales_id} not found"

    return sales_info
from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
# from models import PolicyModel


router = APIRouter()

@router.get("/policies", response_description="List all policies")
async def list_policies(request: Request):
    policies = []
    for doc in await request.app.mongodb["policies"].find().to_list(length=100):
        policies.append(doc)
    return policies

@router.get("/policies/{name}", response_description="Get a single policy")
async def show_policy(name: str, request: Request):
    if (policy := await request.app.mongodb["policies"].find_one({"_id": id})) is not None:
        return policy
    raise HTTPException(status_code=404, detail=f"Policy {name} not found")

# @router.post("/policies", response_description="Add a policy the database")
# async def add_policy(request: Request, policy: PolicyModel = Body(...)):
#     policy = jsonable_encoder(policy)
#     new_policy = await request.app.mogodb["policies"].insert_one(policy)
#     created_policy = await request.app.mongodb["policies"].find_one({ "_id": new_policy.inserted_id })

#     return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_policy)


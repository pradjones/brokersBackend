from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import requests, json
import ast

import os
from dotenv import load_dotenv

settings = load_dotenv()

router = APIRouter()
headers = os.getenv('API_HEADER')
headers = ast.literal_eval(headers)


HOST = 'https://vbrain.visagio.com/api/v1'

@router.get("/repository", response_description="Get Repository List")
async def list_repos():
    path = HOST+'/repository'
    print('path:', path)
    request_result = requests.get(path, headers=headers)
    
    if request_result.status_code == 200:
        repos = json.loads(request_result.content.decode('utf-8'))
    else:
        raise HTTPException(status_code=request_result.status_code, detail=f"Error")
    
    return repos

@router.get("/repository/{id}", response_description="Get Repository Info")
async def get_repo(id: str):
    path = HOST+'/repository/'+id
    print('path:', path)
    request_result = requests.get(path, headers=headers)
    
    if request_result.status_code == 200:
        repos = json.loads(request_result.content.decode('utf-8'))
    else:
        raise HTTPException(status_code=request_result.status_code, detail=f"Error")
    
    return repos

@router.delete("/repository/{id}", response_description="Delete Repository")
async def delete_repo(id: str):
    path = HOST+'/repository/'+id
    print('path:', path)
    request_result = requests.get(path, headers=headers)
    
    if request_result.status_code == 200:
        repos = json.loads(request_result.content.decode('utf-8'))
    else:
        raise HTTPException(status_code=request_result.status_code, detail=f"Error")
    
    return repos
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

@router.get("/job/repo={repo_id}", response_description="Get Jobs List")
async def list_jobs(repo_id : str):
    path = HOST+'/job'
    headers["repository_id"] = repo_id
    request_result = requests.get(path, headers=headers)
    
    if request_result.status_code == 200:
        jobs = json.loads(request_result.content.decode('utf-8'))
    else:
        raise HTTPException(status_code=request_result.status_code, detail=f"Error")
    
    return jobs

@router.get("/job/{id}", response_description="Get Job Info")
async def get_job(id: str):
    path = HOST+'/job/'+id
    request_result = requests.get(path, headers=headers)
    
    if request_result.status_code == 200:
        job_info = json.loads(request_result.content.decode('utf-8'))
    else:
        raise HTTPException(status_code=request_result.status_code, detail=f"Error")
    
    return job_info

@router.get("/job/{id}/result", response_description="Get Job Info")
async def get_result(id: str):
    path = HOST+'/job/'+id+'/result'
    request_result = requests.get(path, headers=headers)
    
    if request_result.status_code == 200:
        job_info = json.loads(request_result.content.decode('utf-8'))
    else:
        raise HTTPException(status_code=request_result.status_code, detail=f"Error")
    
    return job_info



@router.delete("/job/{id}", response_description="Delete Job")
async def delete_job(id: str):
    path = HOST+'/job/'+id
    request_result = requests.get(path, headers=headers)
    
    if request_result.status_code == 200:
        res = json.loads(request_result.content.decode('utf-8'))
    else:
        raise HTTPException(status_code=request_result.status_code, detail=f"Error")
    
    return res
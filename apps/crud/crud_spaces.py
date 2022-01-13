import boto3
from botocore.client import Config

from typing import Generic, TypeVar, Optional, List, Type
from pathlib import Path
from pydantic import BaseModel, env_settings
from pydantic.main import Model

from apps.crud.base import UpdateSchemaType, CreateSchemaType, ModelType
from config import settings

class CRUDSpaces(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    # list all spaces in a region
    def get_spaces(self, client):
        response = client.list_buckets()
        spaces = []
        for space in response["Buckets"]:
            spaces.append(space["Name"])
        return spaces

    # List all files in a space 
    def get_multi(self, client, space_name: str):
        response = client.list_buckets()
        files = []
        for obj in response["Contents"]:
            files.append(obj["Key"])
        return files

    # Get bytes of a file from a space 
    def get(self, client, space_name: str, file_name: str):
        obj = client.get_object(Bucket=space_name, Key=file_name)
        return obj["Body"].read()

    # Download a file from a space
    def download(self, client, space_name: str, file_name: str, destination: str):
        client.download_file(space_name, file_name, destination)

    # upload a file to a space
    def create_file(self, client, space_name: str, location: str, upload_name: Optional[str] = None):
        if upload_name is None:
            upload_name = Path(location).name
            
        client.upload_file(location, space_name, upload_name)

    # upload multiple files to a space
    def create_file(self, client, space_name: str, location: list[str]):
        for loc in location:
            upload_name = Path(location).name
            client.upload_file(loc, space_name, upload_name)

    # update file 
    def update_file(self, client, space_name: str, location: str, file_name: str, new_name: Optional[str] = None):
        client.upload_file(location, space_name, file_name) # update file 
        if new_name is not None:
            # copy to a new name and delete old file
            client.copy_object(Bucket=space_name, CopySource=f"{space_name}/{file_name}", Key=new_name)
            client.delete_object(Bucket=space_name, Key=file_name)
        
    # remove a space 
    def remove(self, client, space_name: str):
        client.delete_bucket(Bucket=space_name)

    # remove a file from a space
    def remove_file(self, client, space_name: str, file_name: str):
        client.delete_object(Bucket=space_name, Key=file_name)

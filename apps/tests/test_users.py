import json 
import random
from sys import api_version
from venv import create

from fastapi.testclient import TestClient

from main import app
from config import settings

client = TestClient(app)

test_user_num = random.randint(15, 995) # Generate a random test number every test to use for the email (Duplicate emails cannot be used to create user)
created_user_id = 0

# Creating users
def test_create_user():
    test_user = {"first_name": "Test", "surname": "User", "email": f"testuser{test_user_num}@visagio.com", "is_superuser": False, "password": "password"}
    response = client.post(f"{settings.API_VERSION}/users", json=test_user)
    data = response.json()
    
    global created_user_id
    created_user_id = data["id"]

    assert response.status_code == 200, response.text

# Creating user with email that already exists
def test_create_duplicate_user():
    test_user = {"first_name": "Naing", "surname": "Lin", "email": f"testuser{test_user_num}@visagio.com", "is_superuser": False, "password": "password"}
    response = client.post(f"{settings.API_VERSION}/users", json=test_user)
    data = response.json()

    assert response.status_code == 400, response.text
    assert data["detail"] == "User with this email already exists"

# reading users
def test_read_user():
    response = client.get(f"{settings.API_VERSION}/users/{created_user_id}")
    data = response.json()
    
    assert response.status_code == 200, response.text
    assert data["email"] == f"testuser{test_user_num}@visagio.com"
    assert data["id"] == created_user_id
    assert data["first_name"] == "Test"  
    assert data["surname"] == "User"
    assert data["is_superuser"] == False

# reading user that does not exist
def test_read_unknown_user():
    unknown_user_id = created_user_id + 1
    response = client.get(f"{settings.API_VERSION}/users/{unknown_user_id}")
    data = response.json()

    assert response.status_code == 404, response.text
    assert data["detail"] == f"User with id {unknown_user_id} not found"

# updating users 
def test_update_user():
    test_user = {"first_name": "Visagio", "surname": "Tester", "email": f"testuser{test_user_num}@visagio.com", "is_superuser": False}
    response = client.put(f"{settings.API_VERSION}/users/{created_user_id}", json=test_user)
    data = response.json()

    assert response.status_code == 200, response.text
    assert data["email"] == f"testuser{test_user_num}@visagio.com"
    assert data["id"] == created_user_id
    assert data["first_name"] == "Visagio"
    assert data["surname"] == "Tester"
    assert data["is_superuser"] == False

# updating user that does not exist
def test_update_unknown_user():
    unknown_user_id = created_user_id + 1
    response = client.get(f"{settings.API_VERSION}/users/{unknown_user_id}")
    data = response.json()

    assert response.status_code == 404, response.text
    assert data["detail"] == f"User with id {unknown_user_id} not found"

# deleting users 
def test_delete_user():
    response = client.delete(f"{settings.API_VERSION}/users/{created_user_id}")
    data = response.json()

    assert response.status_code == 200, response.text
    assert data["email"] == f"testuser{test_user_num}@visagio.com"
    assert data["id"] == created_user_id
    assert data["first_name"] == "Visagio"
    assert data["surname"] == "Tester"
    assert data["is_superuser"] == False

# deleting user that does not exist 
def test_delete_unknown_user():
    response = client.delete(f"{settings.API_VERSION}/users/{created_user_id}")
    data = response.json()

    assert response.status_code == 404, response.text
    assert data["detail"] == f"User with id {created_user_id} not found"
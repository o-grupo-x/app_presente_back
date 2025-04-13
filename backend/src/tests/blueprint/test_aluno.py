from queue import Full
import pytest
import sys
import os
import random
import string
from application import create_app
from flask import Flask

# Debugging line to print sys.path
print(sys.path)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

@pytest.fixture
def app():
    # This fixture sets up the app
    app = create_app('settings.py')  # Ensure settings.py is in src/
    yield app

@pytest.fixture
def client(app):
    # This fixture sets up the test client
    return app.test_client()

def generate_valid_login():
    return ''.join(random.choices(string.ascii_lowercase, k=8))  # 8-letter login

@pytest.fixture
def get_jwt_token(client):  # Ensure the server is running on this URL
    headers = {'Content-Type': 'application/json'}
    payload = {
        "login": "addda",  # Replace with a valid test user
        "senha": "teste123"
    }
    
    # Make the API request to login and get the token
    response = client.post("/api/login", headers=headers, json=payload)
    
    # Check if the response was successful and return the token
    assert response.status_code == 200, f"Login failed: {response.data.decode()}"
    return response.json["JWT"]  # Adjust based on your API's response structure

# GET Tests

# def test_quando_recebe_id_incorreto_entao_retorna_erro(client, get_jwt_token):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {get_jwt_token}'
#     }
    
#     # Send GET request with the Authorization header
#     resposta = client.get("/api/aluno?id=9999999", headers=headers)
    
#     # Print for debugging
#     print("STATUS CODE:", resposta.status_code)
#     print("RESPONSE TEXT:", resposta.data.decode())

#     # Assert the response contains the expected error message
#     assert resposta.status_code == 200  # Adjust if your API returns a different status (e.g., 404)

# def test_quando_recebe_id_entao_retorna_aluno(client, get_jwt_token):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {get_jwt_token}'
#     }

#     # Send GET request with the Authorization header and ID as query parameter
#     resposta = client.get("/api/aluno?id=1", headers=headers)

#     # Print for debugging
#     print("STATUS CODE:", resposta.status_code)
#     print("RESPONSE TEXT:", resposta.data.decode())

#     # Check if the response is in JSON format
#     assert resposta.status_code == 200  # Ensure status code is 200 for success

#     try:
#         response_json = resposta.json  # Parse the response as JSON
#         # Check if the 'Ativo' field exists in the response JSON
#         assert 'Ativo' in response_json.get('status', '')
#     except ValueError:
#         # If the response is not JSON, handle it as a raw string
#         assert "Ativo" in resposta.data.decode()

# def test_quando_recebe_id_invalido_entao_retorna_erro(client, get_jwt_token):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {get_jwt_token}'
#     }
#     resposta = client.get("/api/aluno?id=abc", headers=headers)
#     assert resposta.status_code == 400  # Adjust based on your API
#     assert "Deve ser um número inteiro" in resposta.data.decode()

# def test_dado_ra_retorna_aluno(client, get_jwt_token):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {get_jwt_token}'
#     }
#     resposta = client.get("/api/aluno/findByRa?ra=504084", headers=headers)
#     assert resposta.status_code == 200
#     assert "Ativo" in resposta.data.decode()

# def test_list_all(client, get_jwt_token):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {get_jwt_token}'
#     }
#     resposta = client.get("/api/aluno/listAll", headers=headers)
#     assert resposta.status_code == 200
#     assert "Ativo" in resposta.data.decode()

# PUT Tests

def test_quando_envia_put_sem_id_entao_retorna_erro(client):
    resposta = client.put("/api/aluno")
    assert resposta.status_code == 401

def test_quando_envia_put_sem_body_retorna_erro(client):
    resposta = client.put("/api/aluno?id=2")
    assert resposta.status_code == 401

def test_quando_envia_cadastro_sem_body_entao_retorna_erro(client):
    headers = {'Content-Type': 'application/json'}
    usuario = { 
        "status": "",  
        "login": "",  
        "senha": "",
        "nome": "",
        "cargo": ""
    }
    resposta = client.post("/api/aluno", headers=headers, json=usuario)
    assert resposta.status_code == 401

# DELETE Tests

# def test_quando_envia_delete_com_id_invalido(client, get_jwt_token):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {get_jwt_token}'
#     }
#     resposta = client.delete("/api/aluno?id=foo", headers=headers)
#     assert resposta.status_code == 400  # Adjust based on your API
#     assert "ID deve ser um número inteiro" in resposta.data.decode()

# def test_quando_envia_delete_com_id_inexistente(client, get_jwt_token):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {get_jwt_token}'
#     }
#     resposta = client.delete("/api/aluno?id=9999999", headers=headers)
#     assert resposta.status_code == 404  # Adjust based on your API
#     assert "Aluno não encontrado" in resposta.data.decode()
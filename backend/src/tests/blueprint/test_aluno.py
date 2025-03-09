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
    app = create_app('settings.py')  # Replace 'config.py' with the path to your config file
    yield app  # This will allow the tests to use the app

@pytest.fixture
def client(app):
    # This fixture sets up the test client
    return app.test_client()  # This creates a test client instance of your Flask app

def generate_valid_login():
    return ''.join(random.choices(string.ascii_lowercase, k=8)) # 8-letter login


# @pytest.fixture
# def get_jwt_token(client):  # Ensure the server is running on this URL
#     headers = {'Content-Type': 'application/json'}
#     payload = {
#         "login": "addda",
#         "senha": "teste123"
#     }
    
#     # Make the API request to login and get the token
#     response = client.post("/api/login", headers=headers, json=payload)
    
#     # Check if the response was successful and return the token
#     if response.status_code == 200:
#         return response.json()["JWT"]  # Adjust this based on your API's response structure
#     else:
#         raise Exception("Login failed")

# @pytest.fixture
# def jwt_token():
#     token = get_jwt_token()
#     return token

# def test_quando_recebe_id_incorreto_entao_retorna_erro(client, get_jwt_token):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {get_jwt_token}'  # Use the token from the fixture
#     }
    
#     # Send GET request with the Authorization header
#     resposta = client.get("/api/aluno?id=9999999", headers=headers)
    
#     # Print the status code and response text for debugging
#     print("STATUS CODE:", resposta.status_code)
#     print("RESPONSE TEXT:", resposta.data.decode())

#     # Assert that the response contains the expected error message
#     assert resposta.status_code == 200

#GET

# def test_quando_recebe_id_entao_retorna_aluno(client):
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0MTQwODA3OCwianRpIjoiYjI5MGIwY2MtZmIzYy00ZWNjLTg5ZmYtN2RhZjM5NTA0NGE0IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZF91c3VhcmlvIjo3NCwiSldUIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5Sm1jbVZ6YUNJNlptRnNjMlVzSW1saGRDSTZNVGMwTVRRd09EQTNPQ3dpYW5ScElqb2lPREUxWXpJMk16Z3RaalEzWXkwME9UY3dMV0UxTTJZdFpqQmtZV1ZsWXpaaU1qQmxJaXdpZEhsd1pTSTZJbUZqWTJWemN5SXNJbk4xWWlJNkltRmtaR1JoSWl3aWJtSm1Jam94TnpReE5EQTRNRGM0TENKamMzSm1Jam9pWm1ZeE5Ua3hZamd0T1RCbE9DMDBZV0V4TFRnellUQXRaalZoTkdVMU4yTmxObVJrSWl3aVpYaHdJam94TnpReE5ERTRPRGM0ZlEuc05ZX3drWElueWVPaGQ3YlQ5Mk9BWnhiMlpjR2dncEl0ajlIc1BvMmdDVSIsInVzZXJfaWQiOjc0LCJsb2dpbiI6ImFkZGRhIiwiY2FyZ28iOiJTZWNyZXRhcmlhIiwibm9tZSI6IlRlc3QgVXNlciIsImlkX3NlY3JldGFyaWEiOjcwLCJpZF9wcm9mZXNzb3IiOm51bGwsImlkX2FsdW5vIjpudWxsfSwibmJmIjoxNzQxNDA4MDc4LCJjc3JmIjoiZTlkYzY3ZjMtN2Q3MC00Nzc4LTk0MWUtNjhjY2FjMGFlMGVlIiwiZXhwIjoxNzQxNDE4ODc4fQ.Ei84wTXoi8tV70bN1M-gpYc5w2F6BybMhZELzyG9c2s'  # Ensure the token is valid
#     }

#     # Send GET request with the Authorization header and ID as query parameter
#     resposta = client.get("/api/aluno?id=1", headers=headers)

#     # Print the status code and response text for debugging
#     print("STATUS CODE:", resposta.status_code)
#     print("RESPONSE TEXT:", resposta.data.decode())

#     # Check if the response is in JSON format
#     assert resposta.status_code == 200  # Ensure status code is 200 for success

#     try:
#         response_json = resposta.json  # Parse the response as JSON
#         # Check if the 'Ativo' field exists in the response JSON
#         assert 'Ativo' in response_json.get('status', '')

#     except ValueError:
#         # If the response is not JSON, we handle it as a raw string
#         assert "Ativo" in resposta.data.decode()




# def test_quando_recebe_id_invalido_entao_retorna_erro(client):
#     resposta = client.get("/api/aluno?id=abc")
#     assert "Deve ser um número inteiro" in resposta.text

# def test_dado_ra_retorna_aluno(client):
#     resposta = client.get("/api/aluno/findByRa?ra=504084")
#     assert "Ativo" in resposta.text

# def test_list_all(client):
#     resposta = client.get("/api/aluno/listAll")
#     assert "Ativo" in resposta.text

# #PUT

def test_quando_envia_put_sem_id_entao_retorna_erro(client):
    resposta = client.put("/api/aluno")
    assert resposta.status_code == 401

def test_quando_envia_put_sem_body_retorna_erro(client):
    resposta = client.put("/api/aluno?id=2")
    assert resposta.status_code == 401

def test_quando_envia_cadastro_sem_body_entao_retorna_erro(client):
    headers={'Content-Type': 'application/json'}
    usuario = { 
        "status": "",  
        "login": "",  
        "senha": "",
        "nome": "",
        "cargo": ""
    }
    resposta = client.post("/api/aluno", headers=headers, json=usuario)
    assert resposta.status_code == 401

#DELETE

# def test_quando_envia_delete_com_id_invalido(client):
#     resposta = client.delete("/api/aluno?id=foo")
#     assert "ID deve ser um número inteiro" in resposta.text

# def test_quando_envia_delete_com_id_inexistente(client):
#     resposta = client.delete("/api/aluno?id=9999999")
#     assert "Aluno não encontrado" in resposta.text
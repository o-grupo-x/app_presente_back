# from queue import Full
# import pytest
# import sys
# import os
# import random
# import string


# # Debugging line to print sys.path
# print(sys.path)

# from application import create_app
# from flask import Flask

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

# @pytest.fixture
# def app():
#     # This fixture sets up the app
#     app = create_app('settings.py')  # Replace 'config.py' with the path to your config file
#     yield app  # This will allow the tests to use the app

# @pytest.fixture
# def client(app):
#     # This fixture sets up the test client
#     return app.test_client()  # This creates a test client instance of your Flask app

# def generate_valid_login():
#     return ''.join(random.choices(string.ascii_lowercase, k=8)) # 8-letter login

# # test_usuario.py
# def test_quando_informado_id_correto_deve_retornar_usuario(client):
#     resposta = client.get("/api/usuario?id=3")
#     assert "Login" in resposta.data.decode()  # Make sure to use .data and decode()

# def test_quando_envia_post_sem_body_deve_retornar_erro(client):
    
#     headers = {'Content-Type': 'application/json'}
#     usuario = { 
#         "status": "",  
#         "login": "",  
#         "senha": "",
#         "nome": "",
#         "cargo": ""
#     }
#     resposta = client.post("/api/usuario", headers=headers, json=usuario)
#     assert resposta.status_code == 400


# def test_quando_envia_cadastro_correto_deve_retornar_sucesso(client):
#     headers = {'Content-Type': 'application/json'}

#     usuario = { 
#         "status": True,  
#         "login": generate_valid_login(),  
#         "senha": "teste123",
#         "nome": "Test User",
#         "ra": "",
#         "cargo": "Secretaria"
#     }

#     resposta = client.post("/api/usuario", headers=headers, json=usuario)

#     # Print the status code for debugging
#     print("STATUS CODE:", resposta.status_code)

#     # Check if the status code is 200 (success)
#     assert resposta.status_code == 200

#     # Check if the response contains the expected success message
#     response_data = resposta.get_json()  # Parse the response as JSON
#     assert "id_secretaria" in response_data 
    


# def test_quando_envia_cadastro_de_uma_pessoa_ja_cadastrada_deve_retornar_erro(client):
#     headers = {'Content-Type': 'application/json'}
    
#     usuario = {
#                 "status": True,
#                 "login": "aluco",
#                 "senha": "teste123",
#                 "nome": "Test User",
#                 "ra": "",
#                 "cargo": "Secretaria"
#                 }
#     resposta = client.post("/api/usuario", headers=headers, json=usuario)

#     print("STATUS CODE:", resposta.status_code)
#     print("RESPONSE TEXT:", resposta.data.decode())  # 🔍 Debugging output

#     assert "Esse login já está sendo usado" in resposta.data.decode()
#     assert resposta.status_code == 400

# def test_quando_envia_delete_id_existente_deve_retornar_sucesso(client):
#     resposta = client.delete("/api/usuario?id=3")

#     # Check if the status code is 200 (success)
#     assert resposta.status_code == 200

#     # Check if the response contains the expected success message
#     response_text = resposta.data.decode()
#     assert 'Usuario deletado com sucesso' in response_text


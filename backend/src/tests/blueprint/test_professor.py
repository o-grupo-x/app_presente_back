from queue import Full
import pytest
import sys
import os
import random
import string


# Debugging line to print sys.path
print(sys.path)

from application import create_app
from flask import Flask

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


# GET tests
def test_retornar_professor(client):
    resposta = client.get("/api/professor?id=100")
    assert "Nenhum professor com este ID foi encontrado" in resposta.data.decode()

def test_retorna_um_id_incorreto(client):
    resposta = client.get("/api/professor?id=9999999")
    assert "Nenhum professor com este ID foi encontrado." in resposta.data.decode()

def test_retorna_um_id_invalido(client):
    resposta = client.get("/api/professor?id=hui")
    assert "Deve ser um número inteiro." in resposta.data.decode()

def test_retorna_um_id_negativo(client):
    resposta = client.get("/api/professor?id=-1")
    assert "ID inválido." in resposta.data.decode()

# PUT tests
def test_quando_envia_put_sem_id_entao_retorna_erro(client):
    resposta = client.put("/api/professor")
    assert resposta.status_code == 401
    assert "Nenhum ID enviado" in resposta.data.decode()

def test_quando_envia_put_sem_body_retorna_erro(client):
    resposta = client.put("/api/professor?id=2")
    assert resposta.status_code == 401
    assert "Campo 'nome' inexistente" in resposta.data.decode()

# POST tests
def test_quando_enviar_sem_body(client):
    resposta = client.post("/api/professor")
    assert resposta.status_code == 401
    assert "Campo 'id_usuario' inexistente." in resposta.data.decode()

def test_quando_envia_deve_retornar_sucesso(client):
    headers = {'Content-Type': 'application/json'}
    dados = {
        "id_usuario": 1,
        "nome": "Luiz",
        "status": True
    }
    resposta = client.post("/api/professor", headers=headers, json=dados)
    assert "Professor cadastrado com o id" in resposta.data.decode()

# DELETE tests
def test_delete_professor_inexistente(client):
    resposta = client.delete("/api/professor?id=9999999")
    assert "Professor não encontrado" in resposta.data.decode()

def test_delete_professor_invalido(client):
    resposta = client.delete("/api/professor?id=ety")
    assert "ID deve ser um número inteiro." in resposta.data.decode()

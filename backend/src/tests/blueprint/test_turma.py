import pytest
import sys
import os
from flask import Flask
from src.application import create_app  # Adjust the import to point to the correct path

# Adjust sys.path to include the src directory so the app is importable
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))

@pytest.fixture
def app():
    app = create_app('settings.py')  # Or replace with your config path
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

# POST tests

def test_quando_envia_cadastro_correto_retorna_sucesso(client):
    headers = {'Content-Type': 'application/json'}
    turma = {"nome": "turma2", "ano": 2023, "semestre": 2, "turno": "Noturno", "modalidade": "Presencial", "curso": "Engenharia de Software"}
    resposta = client.post("/api/turma", headers=headers, json=turma)
    assert "Turma Cadastrada com o ID" in resposta.data.decode()

def test_quando_envia_cadastro_sem_body(client):
    headers = {'Content-Type': 'application/json'}
    resposta = client.post("/api/turma", headers=headers)
    assert resposta.status_code == 400

def test_quando_cadastrar_professor_sucesso(client):
    headers = {'Content-Type': 'application/json'}
    turma = {"id_turma": 1, "id_professor": 1}
    resposta = client.post("/api/turma/cadastrarProfessor", headers=headers, json=turma)
    assert "Professor cadastrado" in resposta.data.decode()

def test_quando_cadastrar_aluno_sucesso(client):
    headers = {'Content-Type': 'application/json'}
    turma = {"id_turma": 1, "id_aluno": 1}
    resposta = client.post("/api/turma/cadastrarAluno", headers=headers, json=turma)
    assert "Aluno cadastrado" in resposta.data.decode()

# GET tests

def test_quando_recebe_id_entao_retorna_turma(client):
    resposta = client.get("/api/turma?id=1")
    assert "status" in resposta.data.decode()

def test_quando_recebe_id_incorreto_entao_retornar_error(client):
    resposta = client.get("/api/turma?id=4300")
    assert "Nenhuma turma com o ID" in resposta.data.decode()

def test_quando_recebe_id_invalido_entao_retornar_error(client):
    resposta = client.get("/api/turma?id=aaaaa")
    assert "O ID deve ser um número inteiro" in resposta.data.decode()

def test_quando_recebe_numero_negativo_entao_retorna_error(client):
    resposta = client.get("/api/turma?id=-1")
    assert "ID inválido" in resposta.data.decode()

# PUT tests

def test_quando_edita_retorna_sucesso(client):
    headers = {'Content-Type': 'application/json'}
    turma = {"nome": "turma2", "ano": 2023, "semestre": 2, "turno": "Noturno", "modalidade": "Presencial", "curso": "Engenharia de Software"}
    resposta = client.put("/api/turma?id=1", headers=headers, json=turma)
    assert "sucesso" in resposta.data.decode()

# DELETE tests

def test_quando_envia_delete_id_inexistente_deve_retorna_erro(client):
    resposta = client.delete("/api/turma?id=90000")
    assert "Turma não encontrada" in resposta.data.decode()


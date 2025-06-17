# import pytest
# from src.application import create_app  # Import your app creation function
# from flask import json

# @pytest.fixture
# def client():
#     # Create the app instance for the test
#     app = create_app()
    
#     # Create a test client
#     with app.test_client() as client:
#         yield client

# # GET Tests
# def test_retornar_secretaria(client):
#     resposta = client.get("/api/secretaria?id=500")
#     assert "Nenhum ID encontrado" in resposta.data.decode()

# def test_retorna_um_id_incorreto(client):
#     resposta = client.get("/api/secretaria?id=9999999")
#     assert "Nenhum ID encontrado" in resposta.data.decode()

# def test_retorna_id_invalido(client):
#     resposta = client.get("/api/secretaria?id=oie")
#     assert "ID deve ser um número inteiro." in resposta.data.decode()

# def test_retorna_um_id_negativo(client):
#     resposta = client.get("/api/secretaria?id=-1")
#     assert "ID inválido." in resposta.data.decode()

# # POST Tests
# def test_quando_enviar_sem_body(client):
#     resposta = client.post("/api/secretaria")
#     assert resposta.status_code == 400

# def test_quando_envia_retorna_sucesso(client):
#     headers = {'Content-Type': 'application/json'}
#     dados = {
#         "id_usuario": 1,
#         "status": True,
#         "nome": "Luiz"
#     }
#     resposta = client.post("/api/secretaria", headers=headers, json=dados)
#     assert "Secretaria registrado com o ID" in resposta.data.decode()

# # DELETE Tests
# def test_delete_painel_inexistente(client):
#     resposta = client.delete("/api/secretaria?id=9999999")
#     assert "Secretaria não encontrada" in resposta.data.decode()

# def test_delete_painel_invalido(client):
#     resposta = client.delete("/api/secretaria?id=eyu")
#     assert "ID deve ser um número inteiro." in resposta.data.decode()

# def test_delete_painel_sucesso(client):
#     resposta = client.delete("/api/secretaria?id=1")
#     assert "Secretaria ID" in resposta.data.decode()

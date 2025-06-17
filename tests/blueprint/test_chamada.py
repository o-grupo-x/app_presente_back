import json

# POST

# def test_quando_envia_cadastro_correto_retorna_sucesso(client, auth_headers):
#     headers = {'Content-Type': 'application/json'}
#     headers.update(auth_headers)  # Adicionando token JWT

#     chamada = {
#         "id_turma": 2,
#         "id_professor": 2,
#         "abertura": "2024-06-01T12:00:00",
#         "encerramento": "2024-06-01T14:00:00",
#         "status":"true"  # 🔴 Tente mudar o valor para algo aceito
#     }
#     resposta = client.post("/api/chamada", headers=headers, json=chamada)

#     assert resposta.status_code == 201, f"Erro ao registrar chamada: {resposta.text}"


def test_quando_envia_cadastro_sem_body(client, auth_headers):
    headers = {'Content-Type': 'application/json'}
    headers.update(auth_headers)

    resposta = client.post("/api/chamada", headers=headers)

    assert resposta.status_code == 400
    assert "Bad Request" in resposta.text  

# GET

# def test_quando_recebe_id_entao_retorna_turma(client, auth_headers):
#     resposta = client.get("/api/chamada?id=1", headers=auth_headers)  # 🔴 Mudando para ID 1, que pode existir

#     assert resposta.status_code == 200
#     data = resposta.json
#     assert "status" in data  # Verificando se "status" existe no JSON retornado

def test_quando_recebe_id_incorreto_entao_retornar_error(client, auth_headers):
    resposta = client.get("/api/chamada?id=999999", headers=auth_headers)  # 🔴 Garantindo que não existe

    assert resposta.status_code == 400  
    assert "ID inválido." in resposta.text 

def test_quando_recebe_id_invalido_entao_retornar_error(client, auth_headers):
    resposta = client.get("/api/chamada?id=aaaaaa", headers=auth_headers)

    assert resposta.status_code == 400
    assert "ID incorreto." in resposta.text  

def test_quando_recebe_numero_negativo_entao_retorna_error(client, auth_headers):
    resposta = client.get("/api/chamada?id=-1", headers=auth_headers)

    assert resposta.status_code == 400
    assert "ID incorreto." in resposta.text  

# DELETE

def test_quando_envia_delete_id_inexistente_deve_retornar_erro(client, auth_headers):
    resposta = client.delete("/api/chamada?id=999999", headers=auth_headers)  # 🔴 Garantindo que não existe

    assert resposta.status_code == 400  
    assert "ID inválido." in resposta.text

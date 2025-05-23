# #GET

# def test_retornar_lembrete(client):
#     resposta = client.get("/api/lembrete?id=550097")

#     assert "Nenhum lembrete com este ID foi encontrado" in resposta.text

# def test_retorna_um_id_incorreto(client):
#     resposta = client.get("/api/lembrete?id=999999")
#     assert "Nenhum lembrete com este ID foi encontrado" in resposta.text

# def test_retorna_um_id_invalido(client):
#     resposta = client.get("/api/lembrete?id=abc")
#     assert "ID deve ser um número inteiro." in resposta.text

# def test_retorna_um_id_negativo(client):
#     resposta = client.get("/api/lembrete?id=-1")
#     assert "ID inválido." in resposta.text
# #POST

# def test_quando_enviar_sem_body(client):
#     resposta = client.post("/api/lembrete")

#     assert resposta.status_code == 400

# def test_quando_envia_deve_retornar_sucesso(client):
#     headers={'Content-Type': 'application/json'}
#     dados = {
#         "id_secretaria": 8,
#         "destinatario_cargo": "Professor",
#         "destinatario_id": 123,
#         "titulo": "Lembrete importante",
#         "mensagem": "Não se esqueça da reunião amanhã.",
#         "criacao": "2023-09-29T12:00:00",
#         "visualizacao": None
#     }
#     resposta = client.post("/api/lembrete", headers=headers, json=dados)

#     assert "Lembrete ID" in resposta.text

# #DEL

# def test_delete_lembrete_inexistente(client):
#     resposta = client.delete("/api/lembrete?id=9999999")
#     assert "Lembrete não encontrado" in resposta.text

# def test_delete_lembrete_com_id_invalido(client):
#     resposta = client.delete("/api/lembrete?id=oiu")
#     assert "ID deve ser um número inteiro" in resposta.text
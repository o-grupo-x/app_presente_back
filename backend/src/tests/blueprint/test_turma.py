# def test_quando_envia_cadastro_correto_retorna_sucesso(client, auth_headers):
#     headers = {'Content-Type': 'application/json'}
#     headers.update(auth_headers)  # Adiciona o token JWT

#     turma = {
#         "nome": "turma2", 
#         "ano": 2023, 
#         "semestre": 2, 
#         "turno": "Noturno", 
#         "modalidade": "Presencial", 
#         "curso": "Engenharia de Software"
#     }

#     resposta = client.post("/api/turma", headers=headers, json=turma)
#     assert "Turma Cadastrada com o ID" in resposta.data.decode()

# def test_quando_envia_cadastro_sem_body(client, auth_headers):
#     headers = {'Content-Type': 'application/json'}
#     headers.update(auth_headers)

#     resposta = client.post("/api/turma", headers=headers)
#     assert resposta.status_code == 400

# def test_quando_cadastrar_professor_sucesso(client, auth_headers):
#     headers = {'Content-Type': 'application/json'}
#     headers.update(auth_headers)

#     turma = {"id_turma": 1, "id_professor": 1}
#     resposta = client.post("/api/turma/cadastrarProfessor", headers=headers, json=turma)
#     assert "Professor cadastrado" in resposta.data.decode()

# def test_quando_cadastrar_aluno_sucesso(client, auth_headers):
#     headers = {'Content-Type': 'application/json'}
#     headers.update(auth_headers)

#     turma = {"id_turma": 1, "id_aluno": 1}
#     resposta = client.post("/api/turma/cadastrarAluno", headers=headers, json=turma)
#     assert "Aluno cadastrado" in resposta.data.decode()

# # GET tests
# def test_quando_recebe_id_entao_retorna_turma(client, auth_headers):
#     resposta = client.get("/api/turma?id=1", headers=auth_headers)
#     assert "status" in resposta.data.decode()

# def test_quando_recebe_id_incorreto_entao_retornar_error(client, auth_headers):
#     resposta = client.get("/api/turma?id=4300", headers=auth_headers)
#     assert "Nenhuma turma com o ID" in resposta.data.decode()

# def test_quando_recebe_id_invalido_entao_retornar_error(client, auth_headers):
#     resposta = client.get("/api/turma?id=aaaaa", headers=auth_headers)
#     assert "O ID deve ser um número inteiro" in resposta.data.decode()

# def test_quando_recebe_numero_negativo_entao_retorna_error(client, auth_headers):
#     resposta = client.get("/api/turma?id=-1", headers=auth_headers)
#     assert "ID inválido" in resposta.data.decode()

# # PUT tests
# def test_quando_edita_retorna_sucesso(client, auth_headers):
#     headers = {'Content-Type': 'application/json'}
#     headers.update(auth_headers)

#     turma = {
#         "nome": "turma2", 
#         "ano": 2023, 
#         "semestre": 2, 
#         "turno": "Noturno", 
#         "modalidade": "Presencial", 
#         "curso": "Engenharia de Software"
#     }

#     resposta = client.put("/api/turma?id=1", headers=headers, json=turma)
#     assert "sucesso" in resposta.data.decode()

# # DELETE tests
# def test_quando_envia_delete_id_inexistente_deve_retorna_erro(client, auth_headers):
#     resposta = client.delete("/api/turma?id=90000", headers=auth_headers)
#     assert "Turma não encontrada" in resposta.data.decode()

from flask import Blueprint, request, jsonify,session
import logging
from flask_jwt_extended import jwt_required,create_access_token
import requests, os
from datetime import datetime

from service.UsuarioService import UsuarioService

usuarios = Blueprint("usuario", __name__)

@usuarios.route("/api/usuario", methods=['GET', 'POST', 'PUT', 'DELETE'])
# @jwt_required()
def usuario():
    logging.info('Rota /api/usuario acessada.')
    if request.method == 'GET':
        id_usuario = request.args.get('id')
        try:
            return jsonify(UsuarioService.get_usuario_by_id(id_usuario))
        except AssertionError as error:
            logging.error(f'Erro ao obter usuário por ID: {error}')
            return str(error), 400
        
    if request.method == 'POST':
        data = request.json
                
        status = True
        login = data.get('login', 'NOT_FOUND')
        senha = data.get('senha', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ra = data.get('ra', 'NOT_FOUND')
        cargo = data.get('cargo', 'NOT_FOUND')

        try:
            logging.info('Usuario registrado.')

            return UsuarioService.register(status=status, login=login, senha=senha, nome=nome, ra=ra, cargo=cargo)
        except AssertionError as error:
            logging.error(f'Erro ao registrar usuário: {error}')
            return str(error), 400
        
    if request.method == 'PUT':
        id_usuario = request.args.get('id')
        data = request.json

        status = True
        login = data.get('login', 'NOT_FOUND')
        senha = data.get('senha', 'NOT_FOUND')
        nome = data.get('nome', 'NOT_FOUND')
        ra = data.get('ra', 'NOT_FOUND')
        cargo = data.get('cargo', 'NOT_FOUND')

        try:
            logging.info('Usuario editado.')

            return UsuarioService.update(id_usuario=id_usuario, status=status, login=login, senha=senha, nome=nome, ra=ra, cargo=cargo)
        except AssertionError as error:
            logging.error(f'Erro ao editar usuário por ID: {error}')
            return str(error), 400

    id_usuario = request.args.get('id')
    try:
        # Try to delete the user by ID
        logging.info(f'Trying to delete user with ID: {id_usuario}')
        result = UsuarioService.delete(id_usuario)

        # If successful, return the success message
        return jsonify({"message": "Usuario deletado com sucesso"}), 200

    except ValueError as error:
        # Handle ValueError exceptions (ID issues)
        logging.error(f'Erro ao deletar usuário: {error}')
        return jsonify({"error": str(error)}), 400  # Return as JSON with status 400

    except Exception as error:
        # Catch all other exceptions (unexpected issues)
        logging.error(f'Erro inesperado ao deletar usuário: {error}')
        return jsonify({"error": "Erro interno do servidor"}), 500  # Return as JSON with status 500
        
        
@usuarios.route("/api/login", methods=['POST'])
def login():
    if request.method == 'POST':

        data = request.json
        login = data.get('login', 'NOT_FOUND')
        senha = data.get('senha', 'NOT_FOUND')

        try:
            user = UsuarioService.login(login=login, senha=senha)
            if user : 
                print(user)
                session['user_id'] = user['id_usuario']
                logging.info(f'id_usuario {session}')
                logging.info(f'Usuário {login} logado com sucesso.')
                access_token = create_access_token(identity={
                    'id_usuario': user['id_usuario'],
                    'JWT':user['JWT'],
                    'user_id': user['id_usuario'], 
                    'login': login,
                    'cargo': user['Cargo'],
                    'nome': user['Nome'],
                    'id_secretaria': user.get('id_secretaria'),
                    'id_professor': user.get('id_professor'),
                    'id_aluno': user.get('id_aluno')
                })
                print(user)
                return jsonify(JWT = access_token), 200
            else:
                return jsonify(JWT = access_token), 200
                # return jsonify(error='Login failed'), 401
                
        except AssertionError as error:
            logging.error(f'Erro na tentativa de realizar login: {error}')
            return str(error),400

@usuarios.route("/api/logout", methods=['POST'])
@jwt_required()
def logout():
    try:
        session.clear()
        logging.info('Usuário deslogado com sucesso.')
        return jsonify(message='Logout successful'), 200
    except Exception as e:
        logging.error(f'Erro ao tentar realizar logout: {e}')
        return str(e), 400

# @usuarios.route('/api/log', methods=['POST'])
# def handlelog():
#     print(request.data)
#     if not request.json or 'message' not in request.json or 'level' not in request.json:
#         return jsonify({'error': 'Message and level are required'}), 400

#     log_data = {
#         'message': request.json['message'],
#         'level': request.json['level'],
#         '@timestamp': datetime.now().isoformat()
#     }

#     try:
#         response = requests.post(os.environ['LOGSTASH_HOST'], json=log_data)
#         response.raise_for_status()
#         return jsonify({'status': 'Log sent to Logstash'}), 200
#     except requests.RequestException as error:
#         print(f'Error sending log to Logstash: {error}')
#         return jsonify({'error': 'Failed to send log to Logstash'}), 500
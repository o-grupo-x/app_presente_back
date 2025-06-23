from flask import Blueprint, request, jsonify, session
import logging
from flask_jwt_extended import jwt_required, create_access_token
import requests, os
from datetime import datetime

from service.UsuarioService import UsuarioService

usuarios = Blueprint("usuario", __name__)

@usuarios.route("/usuario", methods=['GET', 'POST', 'PUT', 'DELETE'])
# @jwt_required()
def usuario():
    logging.info('Rota /usuario acessada.')
    if request.method == 'GET':
        id_usuario = request.args.get('id')
        try:
            return jsonify(UsuarioService.get_usuario_by_id(id_usuario))
        except AssertionError as error:
            logging.error(f'Erro ao obter usuário por ID: {error}')
            return jsonify({"error": str(error)}), 400
        
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
            return jsonify({"error": str(error)}), 400
        
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
            return jsonify({"error": str(error)}), 400

    id_usuario = request.args.get('id')
    try:
        logging.info(f'Trying to delete user with ID: {id_usuario}')
        result = UsuarioService.delete(id_usuario)
        return jsonify({"message": "Usuario deletado com sucesso"}), 200
    except ValueError as error:
        logging.error(f'Erro ao deletar usuário: {error}')
        return jsonify({"error": str(error)}), 400
    except Exception as error:
        logging.error(f'Erro inesperado ao deletar usuário: {error}')
        return jsonify({"error": "Erro interno do servidor"}), 500

@usuarios.route("/login", methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 400

    data = request.json
    login = data.get('login', 'NOT_FOUND')
    senha = data.get('senha', 'NOT_FOUND')

    if login == 'NOT_FOUND' or senha == 'NOT_FOUND':
        return jsonify({"error": "Missing login or senha"}), 400

    try:
        user = UsuarioService.login(login=login, senha=senha)
        if user:
            session['user_id'] = user['id_usuario']
            logging.info(f'id_usuario {session}')
            logging.info(f'Usuário {login} logado com sucesso.')
            access_token = create_access_token(identity={
                'id_usuario': user['id_usuario'],
                'user_id': user['id_usuario'],
                'login': login,
                'cargo': user['Cargo'],
                'nome': user['Nome'],
                'id_secretaria': user.get('id_secretaria'),
                'id_professor': user.get('id_professor'),
                'id_aluno': user.get('id_aluno')
            })
            return jsonify({"JWT": access_token}), 200
        else:
            return jsonify({"error": "Login ou senha incorretos"}), 401
    except AssertionError as error:
        logging.error(f'Erro na tentativa de realizar login: {error}')
        return jsonify({"error": str(error)}), 400

@usuarios.route("/logout", methods=['POST'])
@jwt_required()
def logout():
    try:
        session.clear()
        logging.info('Usuário deslogado com sucesso.')
        return jsonify({"message": "Logout successful"}), 200
    except Exception as e:
        logging.error(f'Erro ao tentar realizar logout: {e}')
        return jsonify({"error": str(e)}), 400
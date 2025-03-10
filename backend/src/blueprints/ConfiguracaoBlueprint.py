from flask import Blueprint, request, jsonify
import logging
from flask_jwt_extended import jwt_required
from service.ConfiguracaoService import ConfiguracaoService

configuracoes = Blueprint("configuracoes", __name__)

@configuracoes.route("/api/configuracao", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def configuracao():
    logging.info('Rota /api/configuracao acessada.')

    if request.method == 'GET':
        id_configuracao = request.args.get('id')
        try:
            return jsonify(ConfiguracaoService.get_configuracao_by_id(id_configuracao))
        except AssertionError as error:
            logging.error(f'Erro ao obter configuracao por ID: {error}')

            return str(error), 400
    
    if request.method == 'POST':
        data = request.json

        status = True
        aluno_ausente = data.get('aluno_ausente', 'NOT_FOUND')
        inicio_aula = data.get('inicio_aula', 'NOT_FOUND')
        fim_aula = data.get('fim_aula', 'NOT_FOUND')

        try:
            logging.info('Config registrada.')

            return ConfiguracaoService.register(status=status, aluno_ausente=aluno_ausente, inicio_aula=inicio_aula, fim_aula=fim_aula)
        except AssertionError as error:
            logging.error(f'Erro ao registrar configuracao: {error}')

            return str(error), 400
            
    if request.method == 'PUT':
        id_configuracao = request.args.get('id')
        data = request.json

        status = True
        aluno_ausente = data.get('aluno_ausente', 'NOT_FOUND')
        inicio_aula = data.get('inicio_aula', 'NOT_FOUND')
        fim_aula = data.get('fim_aula', 'NOT_FOUND')

        try:
            logging.info('Config editada.')

            return ConfiguracaoService.update(id_configuracao=id_configuracao, status=status, aluno_ausente=aluno_ausente, inicio_aula=inicio_aula, fim_aula=fim_aula)
        except AssertionError as error:
            logging.error(f'Erro ao editar configuracao por ID: {error}')

            return str(error), 400
        
    if request.method == 'DELETE':
        id_configuracao = request.args.get('id')

        try:
            logging.info('Config deletada.')

            return jsonify(ConfiguracaoService.delete(id_configuracao))
        except AssertionError as error:
            logging.error(f'Erro ao deletar configuracao por ID: {error}')

            return str(error)


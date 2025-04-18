from flask import Blueprint, request, jsonify
import logging

from repository.PresencaRepository import PresencaRepository

from flask_jwt_extended import jwt_required
from service.PresencaService import PresencaService

presencas = Blueprint("presencas", __name__)

@presencas.route("/api/presenca", methods=['GET', 'POST', 'PUT', 'DELETE'])
@jwt_required()
def presencas_main():
    logging.info('Rota /api/presenca acessada.')
    if request.method == 'GET':
        id_presenca = request.args.get('id')
        try:
            return jsonify(PresencaService.get_by_id(id_presenca))
        except AssertionError as error:
            logging.error(f'Erro ao obter presença por ID: {error}')    
            return str(error), 400
    
    if request.method == 'POST':
        data = request.json

        status = True
        id_aluno = data.get('id_aluno', 'NOT_FOUND')
        id_chamada = data.get('id_chamada', 'NOT_FOUND')
        tipo_presenca = data.get('tipo_presenca', 'NOT_FOUND')
        horario = data.get('horario', 'NOT_FOUND')

        try:
            logging.info('Presença registrada.')

            return PresencaService.register(id_aluno=id_aluno, id_chamada=id_chamada, status=status, tipo_presenca=tipo_presenca, horario=horario)
        except AssertionError as error:
            logging.error(f'Erro ao registrar presença: {error}')    
            return str(error), 400
    
    if request.method == 'PUT':
        id_presenca = request.args.get('id')
        data = request.json

        status = True
        id_aluno = data.get('id_aluno', 'NOT_FOUND')
        id_chamada = data.get('id_chamada', 'NOT_FOUND')
        tipo_presenca = data.get('tipo_presenca', 'NOT_FOUND')
        horario = data.get('horario', 'NOT_FOUND')

        try:
            logging.info('Presença editada.')

            return PresencaService.update(id_presenca=id_presenca, id_aluno=id_aluno, id_chamada=id_chamada, status=status, tipo_presenca=tipo_presenca, horario=horario)
        except AssertionError as error:
            logging.error(f'Erro ao editar presença por ID: {error}')    
            return str(error), 400
        
    if request.method == 'DELETE':
        id_presenca = request.args.get('id')
        try:
            logging.info('Presença deletada.')
            
            return jsonify(PresencaService.delete(id_presenca))
        except AssertionError as error:
            logging.error(f'Erro ao deletar presença por ID: {error}')    
            return str(error), 400

@presencas.route("/api/presenca/ra", methods=['POST'])
@jwt_required()
def marcar_presenca_pelo_ra():
    logging.info('Rota /api/presenca/ra acessada.')
    data = request.json

    ra = data.get('ra')
    cargo_manual = data.get('cargo_manual')
    id_manual = data.get('id_manual')

    try:
        return PresencaService.marcar_presenca_pelo_ra(ra, cargo_manual, id_manual)
    except AssertionError as error:
        logging.error(f'Erro ao marcar presença pelo ra: {error}')    
        return str(error), 400

@presencas.route("/api/presenca/listAll", methods=['GET'])
@jwt_required()
def list_all():
    logging.info('Rota /api/presenca/listAll acessada.')
    return PresencaRepository.list_all()

@presencas.route("/api/presenca/findByPresentes", methods=['GET'])
@jwt_required()
def find_by_presentes():
    logging.info('Rota /api/presenca/findByPresentes acessada.')
    return PresencaRepository.find_by_presentes()

@presencas.route("/api/presenca/relatorio", methods=['GET'])
@jwt_required()
def get_attendance_report():
    logging.info('Rota /api/presenca/relatorio acessada.')

    data = request.args.get('data')

    if not data:
        return jsonify({"error": "A data é obrigatória. Use o formato YYYY-MM-DD."}), 400

    try:
        return jsonify(PresencaService.get_attendance_report_by_date(data))
    except AssertionError as error:
        logging.error(f'Erro ao obter relatório de presença: {error}')    
        return str(error), 400

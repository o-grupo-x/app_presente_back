from flask import jsonify
from models import db

from entity.Presenca import Presenca
from entity.Aluno import Aluno
from repository.ChamadaRepository import ChamadaRepository
from datetime import datetime

class PresencaRepository():
    @staticmethod
    def get_presenca_by_id(id):

        try:
            return {
                "id_presenca" : Presenca.query.get(id).id_presenca,
                "aluno": Presenca.query.get(id).id_aluno,
                "chamada": Presenca.query.get(id).id_chamada,
                "status": Presenca.query.get(id).status,
                "tipo_presenca": Presenca.query.get(id).tipo_presenca.value,
                "horario": Presenca.query.get(id).horario
            }
        except AttributeError as error:
            print(f"{str(error)}")
            raise AssertionError ("Prensença não existe.")
    
    @staticmethod
    def list_all():
        presencas = Presenca.query.all()
        resultado = [{
            "Id": p.id,
            "Aluno": p.idAluno.nome,
            "Chamada": p.idChamada,
            "status": p.status,
            "Tipo_presenca": p.tipoPresenca.value,
            "Horario": p.horario
        } for p in presencas]

        return jsonify(resultado)
    
    @staticmethod
    def find_by_presentes():
        presencas = Presenca.query.filter(Presenca.horario.isnot(None)).all()

        resultado = [{
            "Id": p.id,
            "Aluno": p.idAluno.nome,
            "Chamada": p.idChamada,
            "status": p.status,
            "Tipo_presenca": p.tipoPresecna.value,
            "Horario": p.horario
        } for p in presencas]

        return jsonify(resultado)
    
    @staticmethod
    def update(id, data):
        presenca = Presenca.query.get(id)

        presenca.id_aluno = data.id_aluno
        presenca.id_hamada = data.id_chamada
        presenca.status = data.status
        presenca.tipo_presenca = data.tipo_presenca
        presenca.horario = data.horario

        db.session.merge(presenca)
        db.session.commit()
        
        return f"Presenca {id} atualizada!"

    @staticmethod
    def delete(id):
        presenca = Presenca.query.get(id)
        presenca.status = False
        db.session.merge(presenca)
        db.session.commit()

        return {"mensagem":"sucesso"}
    
    @staticmethod
    def marcar_presenca_pelo_ra(ra, cargo_manual, id_manual):
        aluno = db.text(""" Select * from alunos where ra = :ra """)
        
        with db.engine.connect() as connection:
            valor = connection.execute(aluno, {'ra': ra}).fetchone()
      
        valor2 = ChamadaRepository.get_chamadas_abertas_aluno(valor.id_aluno)
        print(valor2)
    
        if not valor2:
            return "Não existe chamada aberta para esse aluno"

        id_aluno = valor.id_aluno

        id_chamada = valor2[0]['id_chamada']

        presenca = db.text(""" SELECT * FROM presencas where id_aluno = :id_aluno and id_chamada = :id_chamada""")
        
        with db.engine.connect() as connection:
            resultado = connection.execute(presenca, {'id_aluno':id_aluno, 'id_chamada':id_chamada}).fetchone()
        
            if resultado is not None:
                return "Presenca já registrada"
            
        if (cargo_manual == "Professor"):
            presenca = Presenca(id_aluno=id_aluno, id_chamada=id_chamada, status=True, horario=datetime.now(), tipo_presenca='Manual', cargo_manual=cargo_manual, id_manual=id_manual)
        elif(cargo_manual == "Secretaria"):
            presenca = Presenca(id_aluno=id_aluno, id_chamada=id_chamada, status=True, horario=datetime.now(), tipo_presenca='Manual', cargo_manual=cargo_manual, id_manual=id_manual)
        db.session.add(presenca)
        db.session.commit()

        return {"mensagem": "presenca registrada"}

    @staticmethod
    def register_presenca(presenca):

        db.session.add(presenca)
        db.session.commit()

        return "Presença realizada!"
    
    @staticmethod
    def get_attendance_by_date(data):
        query = """
            SELECT 
                p.id_presenca,
                a.id_aluno,
                a.nome AS aluno_nome,
                t.nome AS turma_nome,
                m.nome AS materia_nome,
                c.abertura AS chamada_abertura,
                c.encerramento AS chamada_encerramento,
                p.status AS presenca_status,
                p.horario AS presenca_horario,
                p.tipo_presenca
            FROM presencas p
            JOIN chamadas c ON p.id_chamada = c.id_chamada
            JOIN alunos a ON p.id_aluno = a.id_aluno
            JOIN turma_aluno ta ON a.id_aluno = ta.id_aluno
            JOIN turmas t ON ta.id_turma = t.id_turma
            JOIN materias m ON t.id_materia = m.id_materia
            WHERE DATE(c.abertura) = :data
            ORDER BY c.abertura, t.nome, a.nome;
        """

        with db.engine.connect() as connection:
            result = connection.execute(db.text(query), {'data': data}).fetchall()

        attendance_list = [
            {
                "id_presenca": row[0],
                "id_aluno": row[1],
                "aluno_nome": row[2],
                "turma_nome": row[3],
                "materia_nome": row[4],
                "chamada_abertura": row[5].isoformat() if row[5] else None,
                "chamada_encerramento": row[6].isoformat() if row[6] else None,
                "presenca_status": row[7],
                "presenca_horario": row[8].isoformat() if row[8] else None,
                "tipo_presenca": row[9]
            }
            for row in result
        ]

        return attendance_list

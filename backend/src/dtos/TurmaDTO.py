from entity.TurnoEnum import Turno
from entity.ModalidadeEnum import Modalidade
from entity.CursoEnum import Curso
from pydantic import BaseModel

class TurmaDTO(BaseModel):
    id_materia: int
    status: bool
    nome: str
    ano: int
    semestre: int
    turno: Turno
    modalidade: Modalidade
    curso: Curso
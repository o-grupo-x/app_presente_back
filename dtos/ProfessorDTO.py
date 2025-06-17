from pydantic import BaseModel

class ProfessorDTO(BaseModel):
    id_usuario: int
    status: bool
    nome: str
from pydantic import BaseModel

class AlunoDTO(BaseModel):
    id_usuario: int
    status: bool
    ausente: bool
    nome: str
    ra: int
from pydantic import BaseModel

class MateriaDTO(BaseModel):
    status: bool
    nome: str
from pydantic import BaseModel

class SecretariaDTO(BaseModel):
    id_usuario: int
    status: bool
    nome: str
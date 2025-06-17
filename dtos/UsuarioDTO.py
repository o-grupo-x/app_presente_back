from entity.CargoEnum import Cargo
from pydantic import BaseModel
from typing import Optional

class UsuarioDTO(BaseModel):
    status: bool
    login: str
    senha: str
    nome: str
    ra: Optional[int] = None
    cargo: Cargo
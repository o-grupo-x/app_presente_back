from entity.CargoEnum import Cargo
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class LembreteDTO(BaseModel):
    id_secretaria: int
    status: bool
    destinatario_cargo: Cargo
    destinatario_id: int
    titulo: str
    mensagem: str
    criacao: datetime
    visualizacao: Optional[datetime] = None
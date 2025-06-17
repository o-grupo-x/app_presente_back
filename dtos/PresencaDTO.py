from entity.PresencaEnum import TipoPresenca
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class PresencaDTO(BaseModel):
    id_aluno: int
    id_chamada: int
    status: bool
    tipo_presenca: TipoPresenca
    cargo_manual: Optional[str] = None
    id_manual: Optional[int] = None
    horario: datetime
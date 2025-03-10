from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ChamadaDTO(BaseModel):
    id_turma: int
    id_professor: int
    status: bool
    abertura: datetime
    encerramento: Optional[datetime] = None
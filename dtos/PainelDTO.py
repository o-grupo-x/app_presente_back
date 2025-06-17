from datetime import datetime
from pydantic import BaseModel

class PainelDTO(BaseModel):
    id_configuracao: int
    id_secretaria: int
    status: bool
    data_criado: datetime
    total_ativo: int
    total_presentes: int
    total_ausentes: int
    total_presentes_curso: int
    total_ativo_curso: int
    total_ausente_curso: int
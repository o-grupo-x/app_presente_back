from datetime import datetime
from pydantic import BaseModel

class ConfiguracaoDTO(BaseModel):
    status: bool
    aluno_ausente: int
    inicio_aula: datetime
    fim_aula: datetime
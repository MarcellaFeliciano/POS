from pydantic import BaseModel
from typing import List

class Veiculo(BaseModel):
    nome:str
    marca:str
    modelo: str
    placa:str


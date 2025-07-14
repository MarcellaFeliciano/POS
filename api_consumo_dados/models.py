from pydantic import BaseModel

class ConsultaBolsaFamilia(BaseModel):
    cpf: str = None
    nis: str = None
    periodo: str = None  # Formato YYYY-MM

class ConsultaMunicipio(BaseModel):
    municipio: str

class ConsultaGarantiaSafra(BaseModel):
    cpf: str = None
    nis: str = None
    periodo: str = None

class ConsultaSeguroDefeso(BaseModel):
    cpf: str = None
    nis: str = None
    periodo: str = None

class ConsultaServidor(BaseModel):
    cpf: str
from sqlmodel import SQLModel, Field
from typing import Optional

class Pedido(SQLModel, table=True):
    IdPedido: Optional[int] = Field(default=None, primary_key=True)
    ProtocoloPedido: str = Field(index=False)
    Esfera: str = Field(index=False)
    UF: str = Field(index=False)
    Municipio: str = Field(index=False)
    OrgaoDestinatario: str = Field(index=False)
    Situacao: str = Field(index=False)
    DataRegistro: str = Field(index=False)
    PrazoAtendimento: str = Field(index=False)
    FoiProrrogado: str = Field(index=False)
    FoiReencaminhado: str = Field(index=False)
    FormaResposta: str = Field(index=False)
    OrigemSolicitacao: str = Field(index=False)
    IdSolicitante: int = Field(index=False)
    AssuntoPedido: str = Field(index=False)
    SubAssuntoPedido: str = Field(index=False)
    Tag: str = Field(index=False)
    DataResposta: Optional[str] = Field(index=False)
    Decisao: Optional[str] = Field(index=False)
    EspecificacaoDecisao: Optional[str] = Field(index=False)

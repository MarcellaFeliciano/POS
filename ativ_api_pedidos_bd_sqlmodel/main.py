from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, create_engine, Session, select
from typing import Annotated
from contextlib import asynccontextmanager
from models import Pedido
import pandas as pd

# Configuração do banco
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, connect_args={"check_same_thread": False})

# Criar tabela
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Sessão
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

# Carrega CSV no banco
def carregar_csv_para_banco():
    df = pd.read_csv("Pedidos_csv_2025.csv", encoding="utf-16", sep=";")

    # Limpa e padroniza datas em branco
    df = df.fillna("")

    with Session(engine) as session:
        for _, row in df.iterrows():
            pedido = Pedido(
                IdPedido=row["IdPedido"],
                ProtocoloPedido=row["ProtocoloPedido"],
                Esfera=row["Esfera"],
                UF=row["UF"],
                Municipio=row["Municipio"],
                OrgaoDestinatario=row["OrgaoDestinatario"],
                Situacao=row["Situacao"],
                DataRegistro=row["DataRegistro"],
                PrazoAtendimento=row["PrazoAtendimento"],
                FoiProrrogado=row["FoiProrrogado"],
                FoiReencaminhado=row["FoiReencaminhado"],
                FormaResposta=row["FormaResposta"],
                OrigemSolicitacao=row["OrigemSolicitacao"],
                IdSolicitante=int(row["IdSolicitante"]),
                AssuntoPedido=row["AssuntoPedido"],
                SubAssuntoPedido=row["SubAssuntoPedido"],
                Tag=row["Tag"],
                DataResposta=row["DataResposta"] if row["DataResposta"] else None,
                Decisao=row["Decisao"] if row["Decisao"] else None,
                EspecificacaoDecisao=row["EspecificacaoDecisao"] if row["EspecificacaoDecisao"] else None
            )
            session.add(pedido)
        session.commit()

# Inicialização FastAPI com carregamento do banco
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    carregar_csv_para_banco()
    yield

app = FastAPI(lifespan=lifespan)

# Rota para buscar pedido
@app.get("/pedidos/{pedido_id}", response_model=Pedido)
def buscar_pedido(pedido_id: int, session: SessionDep):
    pedido = session.exec(select(Pedido).where(Pedido.IdPedido == pedido_id)).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

## Aulas de Programação Orientada a Serviços



 """
    from typing import List, Annotated
from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from sqlmodel import SQLModel, Session, create_engine, select
from models import Loja, Usuario, Produto, Pedido, PedidoProduto, Avaliacao

# Banco
url = "sqlite:///banco.db"
engine = create_engine(url, echo=True)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(lifespan=lifespan)

# Rotas FastAPI
@app.get("/lojas", response_model=List[Loja])
def listar_lojas(session: Session = SessionDep):
    return session.exec(select(Loja)).all()
from fastapi import FastAPI, HTTPException
from models import Usuario, Produto, Loja, Pedido, Avaliacao
from typing import List

app = FastAPI()

usuarios:List[Usuario] = []
produtos: List[Produto] = []
pedidos:List[Pedido] = []
avaliacoes:List[Avaliacao] = []

lojas:List[Loja] = []


# listar lojas
@app.get("/lojas", response_model=List[Loja])
def listar_lojas():
    return lojas
    
    """

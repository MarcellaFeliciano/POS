from fastapi import FastAPI,HTTPException
from models import Veiculo  
from typing import List

app = FastAPI()
veiculos:List[Veiculo]=[]

@app.get("/veiculos",response_model=List[Veiculo])
def listar_veiculos():
    return veiculos


@app.get("/veiculos/{placa}",response_model=Veiculo)
def listar_veiculo(placa:str):
    for veiculo in veiculos:
        if veiculo.placa == placa:
            return veiculo
    raise HTTPException(404,"Não localizado")


@app.post("/veiculos", response_model=Veiculo)
def criar_veiculo(veiculo:Veiculo):
    veiculos.append(veiculo)
    return veiculo
    raise HTTPException(404,"Não localizado")


@app.delete("/veiculos/{placa}",response_model=Veiculo)
def deletar_veiculo(placa:str):
    for id, veiculo in enumerate(veiculos):
        if veiculo.placa == placa:
            veiculos.pop(id)
            return veiculos
    raise HTTPException(404,"Não localizado")


@app.put("/veiculos/{placa}",response_model=Veiculo)
def editar_veiculos(placa:str, atu_veiculo:Veiculo):
    for id, veiculo in enumerate(veiculos):
        if veiculo.placa == placa:
            veiculos[id] = atu_veiculo
            return veiculo
    raise HTTPException(404,"Não localizado")
from fastapi import FastAPI, HTTPException
from models import Usuario, Livro, Emprestimo, Biblioteca
from typing import List

app = FastAPI()
usuarios:List[Usuario] = []
livros:List[Livro] = []
emprestimos:List[Emprestimo]

Bibliotecas: List[Biblioteca] = []
@app.get("/bibliotecas", response_model=List[Biblioteca])
def listar_bibliotecas():
    return bibliotecas

@app.get("/bibliotecas/{nome}", response_model=Biblioteca)
def listar_bibliotecas(nome:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == nome:
        return biblioteca

     raise HTTPException(404, "Não achei")


@app.post("/bibliotecas")
def cadastrar_bibliotecas(nome:str):
    data = {
        "nome":nome,
        "acervo":[],
        "usuarios":[],
        "emprestimos":[]
    }
    biblioteca = Biblioteca(data)
    biblioteca.append(biblioteca)




@app.delete("bibliotecas/{nome}", response_model=Biblioteca)
def excluir_usuario(nome:str):
    for id,bibli in enumerate(bibliotecas):
        if bibli.nome == nome:
            bibliotecas.pop(id)
            return usuario

    raise HTTPException(404, "Não achei")
    


@app.get("usuarios/{biblioteca}", response_model=List[Usuario])
def listar_usuarios(biblioteca:str):
    for biblioteca in bibliotecas:
        if biblioteca.nome == biblioteca:
            return biblioteca.usuarios
    raise HTTPException(404, "Não achei")


@app.get("usuarios/{username}", response_model=List[Usuario])
def listar_usuarios(username:str):
    for usuario in usuarios:
        if usuario.username == username:
            return usuario
    raise HTTPException(404, "Não achei")


@app.post("usuarios", response_model=Usuario)
def criar_usuario(usuario:Usuario):
    usuarios.append(usuario)
    return usuario


@app.delete("usuarios/{username}", response_model=Usuario)
def excluir_usuario(username:str):
    for id,user in enumerate(usuarios):
        if user.username == username:
            usuarios.pop(id)
            return usuario

    raise HTTPException(404, "Não achei")
    


@app.get("livros", response_model=List[Livro])
def listar_livros():
    return livros


@app.get("livros/{titulo}", response_model=List[Livro])
def listar_livros(nome:str,titulo:str):
    for livro in livros:
        if livro.titulo == titulo:                                                                                                                                                                                                                                                                                                                                                                  
            return livro
    raise HTTPException(404, "Não achei")


@app.post("livros", response_model=Livro)
def criar_livro(livro:livro):
    livros.append(livro)
    return livro


@app.delete("livros/{titulo}", response_model=Livro)
def excluir_livro(titulo:str):
    for id,liv in enumerate(livros):
        if liv.titulo == titulo:
            livros.pop(id)
            return livro

    raise HTTPException(404, "Não achei")
    


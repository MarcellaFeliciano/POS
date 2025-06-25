import requests # pip install requests
import time
from colorama import Fore # pip install colorama

def listar():
    request = requests.get("http://127.0.0.1:8000/livros")
    print(request.text)
    livros = request.json()

    if request.status_code == 200:
        return livros
    else: 
        return None
    

def pesquisar(pesquisa):
    request = requests.get(f'http://127.0.0.1:8000/livros/{pesquisa}')
    livro = request.json()

    if request.status_code == 200:
        return livro
    else:
        return None
    

def cadastrar(titulo, ano, edicao):
    liv = {"titulo":titulo, "ano":ano, "edicao":edicao}
    add=requests.post(f'http://127.0.0.1:8000/livros',json=liv)

    if add.status_code == 200:
        msg = Fore.GREEN +f"{titulo} adicionado com sucesso a lista de livros!"+Fore.WHITE
        return msg
    else:
        msg = Fore.RED +f"Não foi possível adicionar {titulo} a lista de livros, tente novamente!"+Fore.WHITE
        return msg
    
def apagar(titulo):
    request = requests.delete(f'http://127.0.0.1:8000/livros/{titulo}')
    
    if request.status_code == 200:
        return Fore.GREEN +"Livro apagado com sucesso!"+Fore.WHITE
    else:
        return Fore.RED +"Não foi possível apagar o livro!"+Fore.WHITE
    

def editar(titulo, liv_atu):
    edi = requests.put(f'http://127.0.0.1:8000/livros/{titulo}', json=liv_atu)
    print(edi.status_code)

    if edi.status_code == 200:
        return edi.json()
    else: 
        return None 

if __name__ == "__main__":
    while True:
        print()
        print(("-"*10)+Fore.LIGHTCYAN_EX+" M E N U "+Fore.WHITE+("-"*10))
        print(" [1] - Listar todos os livros")
        print(" [2] - Pesquisar livro")
        print(" [3] - Cadastrar livro")
        print(" [4] - Deletar livro")
        print(" [5] - Editar livro")
        print(" [6] - Sair")

        print("-"*29)
        comando = int(input(Fore.LIGHTYELLOW_EX +"- Escolha uma opção: "+Fore.WHITE))


        if comando == 1:
            lista_livros = listar()

            if lista_livros:
                print("-"*30)
                print("  L I S T A  D E  L I V R O S")
                for n,liv in enumerate(lista_livros):
                    print("-="*15)
                    print(" "*12+f"Livro {n+1}")
                    print("-="*15)
                    print(f" Titulo: {liv['titulo']}")
                    print(f" Ano: {liv['ano']}")
                    print(f" Edição: {liv['edicao']}")
            time.sleep(2)
                    

        if comando == 2:
            print("-"*30)
            print()
            print("-"*10+" PESQUISAR "+"-"*10)
            titulo = str(input(f"- Digite o titulo do livro: "))
            livro = pesquisar(titulo)

            print(Fore.LIGHTBLACK_EX+"Buscando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)
            
            
            if livro:
                print("-"*30)
                print(" "*10+f"Livro Encontrado")
                print("-"*30)
                print(f" Titulo: {livro['titulo']}")
                print(f" Ano: {livro['ano']}")
                print(f" Edição: {livro['edicao']}")

            else:
                print("-="*15)
                print(Fore.RED+"Livro não encontrado!"+Fore.WHITE)
            time.sleep(2)
        

        if comando == 3:
            print("-="*2+" Informações do Livro "+"-="*2)
            titulo = str(input(' - Digite o título do livro: '))
            ano = int (input(' - Digite o ano: '))
            edicao = int(input(' - Digite a edição: '))
            add_livro = cadastrar(titulo=titulo, ano=ano, edicao=edicao)

            print("-"*30)
            print(add_livro)

        if comando == 4:
            print("-="*4+" APAGAR REGISTRO "+"-="*4)
            titulo = str(input(' - Digite o título do livro: '))
            status = apagar(titulo)
            
            print(Fore.LIGHTBLACK_EX+"Apagando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)

            print("-="*15)
            print(status)


        if comando == 5:
            print("-="*4+" Editar Livro "+"-="*4)
            titulo = str(input("Digite o titulo do livro: "))

            livro = pesquisar(titulo)

            if livro:
                print("-"*2+" Editar Informações "+"-"*2)
                print(" *Caso não queira alterar [ENTER]*")
                print()
                titulo_edi = str(input(f' - Editar título do livro ({livro['titulo']}): '))
                ano_edi = str(input(f' - Editar o ano ({livro['ano']}): '))
                edicao_edi = str(input(f' - Editar a edição ({livro['edicao']}): '))

                if titulo_edi == "":
                    titulo_edi = livro['titulo']
                if ano_edi == "":
                    ano_edi = livro['ano']
                if edicao_edi == "":
                    edicao_edi = livro['edicao']
                
                liv_atu = {"titulo":titulo_edi, "ano":int(ano_edi), "edicao":int(edicao_edi)}

                print("-"*30)
                edicao = editar(titulo=titulo,liv_atu=liv_atu)

                if edicao:
                    print("Edicao concluida") 
                else:
                    print("não foi possivel editar")
                


        if comando == 6:

            print(Fore.LIGHTRED_EX+"Saindo", end='')
            for i in range(3):
                print(".", end='', flush=True)  
                time.sleep(0.5)
            print(Fore.WHITE)
            break

import requests # pip install requests
import time
from colorama import Fore # pip install colorama

def listar():
    request = requests.get("http://127.0.0.1:8000/veiculos")
    print(request.text)
    veiculos = request.json()

    if request.status_code == 200:
        return veiculos
    else: 
        return None
    

def pesquisar(pesquisa):
    request = requests.get(f'http://127.0.0.1:8000/veiculos/{pesquisa}')
    veiculo = request.json()

    if request.status_code == 200:
        return veiculo
    else:
        return None
 
def cadastrar(nome, marca, modelo, placa):
    liv = {"nome":nome, "marca":marca, "modelo":modelo, "placa":placa}
    add=requests.post(f'http://127.0.0.1:8000/veiculos',json=liv)

    if add.status_code == 200:
        msg = Fore.GREEN +f"{nome} adicionado com sucesso a lista de livros!"+Fore.WHITE
        return msg
    else:
        msg = Fore.RED +f"Não foi possível adicionar {nome} a lista de livros, tente novamente!"+Fore.WHITE
        return msg
    
def apagar(placa):
    request = requests.delete(f'http://127.0.0.1:8000/veiculos/{placa}')
    
    if request.status_code == 200:
        return Fore.GREEN +"Veiculo apagado com sucesso!"+Fore.WHITE
    else:
        return Fore.RED +"Não foi possível apagar o veiculo!"+Fore.WHITE

def editar(placa, veiculo_atu):
    edi = requests.put(f'http://127.0.0.1:8000/veiculos/{placa}', json=veiculo_atu)
    print(edi.status_code)

    if edi.status_code == 200:
        return edi.json()
    else: 
        return None 


if __name__ == "__main__":
    while True:
        print()
        print(("-"*10)+Fore.LIGHTCYAN_EX+" M E N U "+Fore.WHITE+("-"*10))
        print(" [1] - Listar todos os veiculos")
        print(" [2] - Cadastrar veiculo")
        print(" [3] - Deletar veiculo")
        print(" [4] - Editar veiculo")
        print(" [5] - Sair")

        print("-"*29)
        comando = int(input(Fore.LIGHTYELLOW_EX +"- Escolha uma opção: "+Fore.WHITE))


        if comando == 1:
            lista_veiculos = listar()
            if lista_veiculos:
                print("-"*30)
                print(" L I S T A  D E  V E I C U L O S")
                for n,veic in enumerate(lista_veiculos):
                    print("-="*15)
                    print(" "*12+f"Veiculo {n+1}")
                    print("-="*15)
                    print(f" Nome: {veic['nome']}")
                    print(f" Marca: {veic['marca']}")
                    print(f" Modelo: {veic['modelo']}")
                    print(f" Placa: {veic['placa']}")
            time.sleep(2)

        if comando == 2:

            print("-="*2+" Informações do Veiculo "+"-="*2)
            nome = str(input(' - Digite o nome do veiculo: '))
            marca = str (input(' - Digite a marca: '))
            modelo = str(input(' - Digite o modelo: '))

            lista_veiculos = listar()
        
            placas = []
            placa = str(input(' - Digite a placa: '))
            for veiculo in lista_veiculos:
                placas.append({veiculo['placa']})

            while True:
                if placa in placas:
                    print('Essa placa já está cadastrada!')
                    placa = str(input(' - Digite a placa novamente: '))
                else:
                    break


            add_veiculo = cadastrar(nome=nome, marca=marca, modelo=modelo, placa=placa)

            print("-"*30)
            print(add_veiculo)

        
        if comando == 3:
            print("-="*4+" APAGAR REGISTRO "+"-="*4)
            placa = str(input(' - Digite a placa do veiculo: '))
            status = apagar(placa)
            
            print(Fore.LIGHTBLACK_EX+"Apagando", end='')
            for i in range(2):
                print(".", end='', flush=True) 
                time.sleep(0.5)
            print()
            print(Fore.WHITE)

            print("-="*15)
            print(status)

        if comando == 4:
            print("-="*4+" Editar Veiculo "+"-="*4)
            placa = str(input("Digite a placa do veiculo: "))

            veiculo = pesquisar(placa)

            if veiculo:
                print("-"*2+" Editar Informações "+"-"*2)
                print(" *Caso não queira alterar [ENTER]*")
                print()
                nome_edi = str(input(f' - Editar nome do veiculo ({veiculo['nome']}): '))
                marca_edi = str(input(f' - Editar a marca ({veiculo['marca']}): '))
                modelo_edi = str(input(f' - Editar o modelo ({veiculo['modelo']}): '))
                placa_edi = str(input(f' - Editar a placa ({veiculo['placa']}): '))


                if nome_edi == "":
                    nome_edi = veiculo['nome']
                if marca_edi == "":
                    marca_edi = veiculo['marca']
                if modelo_edi == "":
                    modelo_edi = veiculo['modelo']
                if placa_edi == "":
                    placa_edi = veiculo['placa']
                
                veiculo_atu = {"nome":nome_edi, "marca":marca_edi, "modelo":modelo_edi, "placa":placa_edi}

                print("-"*30)
                edicao = editar(placa=placa,veiculo_atu=veiculo_atu)

                if edicao:
                    print("Edicao concluida") 
                else:
                    print("não foi possivel editar")
                





import httpx

def fetch_data(url: str, params: dict):
    response = httpx.get(url, params=params)
    response.raise_for_status()  # Levanta um erro para códigos de resposta de erro
    return response.json()

def main():
    print("Bem-vindo ao sistema de consulta do Portal da Transparência!")
    cpf = input("Digite o CPF: ")

    while True:
        print("\nEscolha uma opção:")
        print("1. Consultar Bolsa Família")
        print("2. Consultar Bolsa Família por Município")
        print("3. Consultar Garantia-Safra")
        print("4. Consultar Seguro Defeso")
        print("5. Consultar Servidor do Executivo Federal")
        print("0. Sair")
        
        choice = input("Opção: ")

        if choice == "1":
            nis = input("Digite o NIS (ou deixe em branco): ")
            periodo = input("Digite o período (YYYY-MM, ou deixe em branco): ")
            url = "http://api.portaldatransparencia.gov.br/bolsa_familia"
            params = {"cpf": cpf, "nis": nis or None, "periodo": periodo or None}
            data = fetch_data(url, params)
            print(data)

        elif choice == "2":
            municipio = input("Digite o município: ")
            url = "http://api.portaldatransparencia.gov.br/bolsa_familia/municipio"
            params = {"municipio": municipio}
            data = fetch_data(url, params)
            print(data)

        elif choice == "3":
            nis = input("Digite o NIS (ou deixe em branco): ")
            periodo = input("Digite o período (YYYY-MM, ou deixe em branco): ")
            url = "http://api.portaldatransparencia.gov.br/garantia_safra"
            params = {"cpf": cpf, "nis": nis or None, "periodo": periodo or None}
            data = fetch_data(url, params)
            print(data)

        elif choice == "4":
            nis = input("Digite o NIS (ou deixe em branco): ")
            periodo = input("Digite o período (YYYY-MM, ou deixe em branco): ")
            url = "http://api.portaldatransparencia.gov.br/seguro_defeso"
            params = {"cpf": cpf, "nis": nis or None, "periodo": periodo or None}
            data = fetch_data(url, params)
            print(data)

        elif choice == "5":
            url = "http://api.portaldatransparencia.gov.br/servidor"
            params = {"cpf": cpf}
            data = fetch_data(url, params)
            print(data)

        elif choice == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
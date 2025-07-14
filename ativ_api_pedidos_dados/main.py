from fastapi import FastAPI, HTTPException
import pandas as pd
import uvicorn
import threading

app = FastAPI()

# carregar os dados do arquivo csv
def load_data():
    return pd.read_csv('Pedidos_csv_2025.csv', sep=';', encoding='utf-16')

# Rota da API para obter os detalhes do pedido
@app.get("/pedido/{pedido_id}")
def get_pedido(pedido_id: int):
    df = load_data()
    
    # Verificar se o pedido_id existe
    pedido = df[df['IdPedido'] == pedido_id]
    
    if pedido.empty:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")

    return pedido.to_dict(orient='records')[0]

# Função para a aplicação de terminal
def terminal_app():
    df = load_data()
    while True:
        pedido_id = input("Digite o ID do pedido (ou 'sair' para encerrar): ")
        if pedido_id.lower() == 'sair':
            break
        try:
            pedido_id = int(pedido_id)
            pedido = df[df['IdPedido'] == pedido_id]
            if pedido.empty:
                print("Erro 404: Pedido não encontrado")
            else:
                print("\nDetalhes do Pedido:")
                pedido_info = pedido.to_dict(orient='records')[0]
                for key, value in pedido_info.items():
                    print(f"{key}: {value}")
                print()  # Linha em branco para espaçamento
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == '__main__':
    # Execute a API em uma thread separada
    threading.Thread(target=lambda: uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")).start()
    
    # Execute a aplicação de terminal
    terminal_app()
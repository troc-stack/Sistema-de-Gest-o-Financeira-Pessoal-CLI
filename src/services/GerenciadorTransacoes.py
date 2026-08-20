import json

class Gerenciador:

    def __init__(self):
        try:
            with open("transacoes.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return 'Não há dados registrados'    
        else: 
            self.__dados = dados

    def listar(self):
        n = 0 

        print("--- LISTA DE TRANSAÇÕES ---")
        for elemento in self.__dados['transações']:
            n += 1
            print('--' * 30)
            print(f'transação de número {n}')
            print('--' * 30)
            print(f"| ID: {elemento['id']} "
                f"| Tipo: {elemento['tipo']} "
                f"| Valor: R$ {elemento['valor']:.2f} "
                f"| Categoria: {elemento['categoria']} "
                f"| Data: {elemento['data']}")
            print('--' * 30)

    def editar(self):
        pass

    def excluir(self):
        pass
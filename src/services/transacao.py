import json

class Transacoes:

    def __init__(self, Id, Tipo, valor, categoria, data):
        self.__Id = Id 
        self.__Tipo = Tipo 
        self.__valor = valor 
        self.__categoria = categoria
        self.__data = data 

    def salvar_arquivo(self):
        nova_transacao = {
            { 'id': self.__Id, 'tipo': self.__Tipo, 'valor': self.__valor, 'categoria' : self.__categoria, 'data': self.__data}
            }

        try:
            with open("transacoes.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            dados = {"transações": []}

        dados["transações"].append(nova_transacao)

   
        with open("transacoes.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
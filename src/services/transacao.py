
class Transacoes:

    def __init__(self, Id, Tipo, descricao, valor, categoria, data):
        self.__Id = Id 
        self.__Tipo = Tipo 
        self.__descrição = descricao
        self.__valor = valor 
        self.__categoria = categoria
        self.__data = data 

    def salvar_arquivo():
        try: 
            with open("transacoes.json", "r", encoding="utf-8") as arquivo: 
                dados = json.load(arquivo)
        except FileNotFoundError:
            print('arquivo não encontrado!')
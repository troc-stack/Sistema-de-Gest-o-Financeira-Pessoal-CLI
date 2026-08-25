import json
from datetime import datetime
from services import GerenciadorTransacoes

class Validar:

    @staticmethod
    def pedir_id():
        while True: 
            id = input('Digite um valor: ')

            id = Validar.validar_id(id)

            if id is not None:
                return id

            print('ID digitado não e válido')

    @staticmethod
    def validar_id(id):

        try: 
            id = int(id)  

        except ValueError:
            return None

        rr = GerenciadorTransacoes
        if rr.id_transacao_existe(id) is True:
            return None

        return id

    @staticmethod
    def pedir_valor(tipo):
        while True:
            valor = input('Digite o valor da transação: R$ ')

            valor = Validar.validar_valor(valor, tipo)

            if valor is not None: 
                if tipo == 'Receita':
                    valor = abs(valor)
                elif tipo == 'Despesa':
                    valor = -abs(valor)
                return valor
            
            print('Valor digitado não e valido')

    @staticmethod
    def validar_valor(valor):

        try:
            valor = float(valor)

            if valor <= 0:
                return None

            return valor

        except ValueError:
            return None

    @staticmethod
    def pedir_categoria():
        while True:
            categoria = input('Digite a categoria da transação, de 2 a 30 caracteres: ')

            categoria = Validar.validar_categoria(categoria)

            if categoria is not None:
                return categoria

            print('Categoria digitada não e valida')

    @staticmethod
    def validar_categoria(categoria):

        categoria = categoria.strip().title()

        if len(categoria) < 2 or len(categoria) > 30:
            print("Erro: A categoria deve ter entre 2 e 30 caracteres.")
            return None

        if any(char.isdigit() for char in categoria):
            print("Erro: A categoria não pode conter números.")
            return None

        return categoria

    @staticmethod
    def pedir_data():
        while True:
            data = input('Digite a data da transação (dd/mm/aaaa): ')

            data = Validar.validar_data(data)

            if data is not None:
                return data

            print('Data digitada não e valida')

    @staticmethod
    def validar_data(data):

        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            return None

    @staticmethod
    def pedir_id_existente(): 
        id = input('Digite o ID: ')

        rr = GerenciadorTransacoes
        if rr.id_transacao_existe(id) is False:
            return id

        print('ID digitado não e válido')
        return None 
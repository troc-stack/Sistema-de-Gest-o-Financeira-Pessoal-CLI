import json
from datetime import datetime
from services import GerenciadorTransacoes

def pedir_id():
    while True: 
        id = input('Digite o ID: ')

        id = validar_id(id)

        if id is not None and id != True:
            return id

        elif id is True:
            print('1 - Tentar outro ID')
            print('2 - Cancelar cadastro')

            while True:
                try:
                    resp = int(input('Escolha uma das opçoes com 1 ou 2: '))
                    if resp in (1,2):
                        break
                except TypeError:
                    print('valor digitado não e valido')

            if resp == 2:
                return None 
            else: 
                continue

        print('ID digitado não e válido')

def validar_id(id):

    try: 
        id = int(id)  

    except ValueError:
        return None

    rr = GerenciadorTransacoes.Gerenciador()
    if rr.id_transacao_existe(id) is True:
        print('ID informado ja esta em uso')
        return True

    return id

def pedir_valor(tipo):
    while True:
        valor = input('Digite o valor da transação(apenas números): R$ ')

        valor = validar_valor(valor)

        if valor is not None: 
            if tipo == 'Receita':
                valor = abs(valor)
            elif tipo == 'Despesa':
                valor = -abs(valor)
            return valor
        
        print('Valor digitado não e valido')

def validar_valor(valor):

    try:
        valor = abs(float(valor))

        if valor <= 0:
            return None

        return valor

    except ValueError:
        return None

def pedir_categoria():
    while True:
        categoria = input('Digite a categoria da transação, de 2 a 30 caracteres: ')

        categoria = validar_categoria(categoria)

        if categoria is not None:
            return categoria

        print('Categoria digitada não e valida')

def validar_categoria(categoria):

    categoria = categoria.strip().title()

    if len(categoria) < 2 or len(categoria) > 30:
        print("Erro: A categoria deve ter entre 2 e 30 caracteres.")
        return None

    if any(char.isdigit() for char in categoria):
        print("Erro: A categoria não pode conter números.")
        return None

    return categoria

def pedir_data():
    while True:
        data = input('Digite a data da transação (dd/mm/aaaa): ')

        data = validar_data(data)

        if data is not None:
            return data

        print('Data digitada não e valida')

def validar_data(data):

    try:
        datetime.strptime(data, "%d/%m/%Y")
        return data
    except ValueError:
        return None

def pedir_id_existente():
    while True: 
        id = input('Digite o ID: ')

        id = validar_id_existente(id)

        if id is not None and id != False:
            return id

        elif id is False:
            print('1 - Tentar outro ID')
            print('2 - Cancelar ')

            while True:
                try:
                    resp = int(input('Escolha uma das opçoes com 1 ou 2: '))
                    if resp in (1,2):
                        break
                except TypeError:
                    print('valor digitado não e valido')

            if resp == 2:
                return None 
            else: 
                continue

        print('ID digitado não e válido')

def validar_id_existente(id):

    try: 
        id = int(id)  

    except ValueError:
        return None

    rr = GerenciadorTransacoes.Gerenciador()
    if rr.id_transacao_existe(id) is False:
        print('ID informado não existe')
        return False

    return id
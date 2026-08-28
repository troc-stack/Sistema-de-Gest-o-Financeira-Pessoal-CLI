import json
from datetime import datetime
from services import GerenciadorTransacoes

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

def validar_valor(valor):

    try:
        valor = abs(float(valor))

        if valor <= 0:
            return None

        return valor

    except ValueError:
        return None

def validar_categoria(categoria):

    categoria = categoria.strip().title()

    if len(categoria) < 2 or len(categoria) > 30:
        print("Erro: A categoria deve ter entre 2 e 30 caracteres.")
        return None

    if any(char.isdigit() for char in categoria):
        print("Erro: A categoria não pode conter números.")
        return None

    return categoria


def validar_data(data):

    try:
        datetime.strptime(data, "%d/%m/%Y")
        return data
    except ValueError:
        return None

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

def pedir_opcao():
    while True:
        a = input('Digite o numero opção desejada: ')
        a = validar_opção(a)

        if a is not None: 
            return a

        print('valor digitado e invalido tente novamente')

def validar_opção(a):
    while True:
        try:
            a = int(a)
            return a

        except TypeError:
            print('Erro: Digite um numero inteiro')
            return None
        
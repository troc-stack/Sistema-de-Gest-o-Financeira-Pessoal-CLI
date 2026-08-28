from utils import validacoes

def pedir_id():
    while True: 
        id = input('Digite o ID: ')

        id = validacoes.validar_id(id)

        if id is not None and id != True:
            return id

        elif id is True:
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

def pedir_valor(tipo):
    while True:
        valor = input('Digite o valor da transação(apenas números): R$ ')

        valor = validacoes.validar_valor(valor)

        if valor is not None: 
            if tipo == 'Receita':
                valor = abs(valor)
            elif tipo == 'Despesa':
                valor = -abs(valor)
            return valor
        
        print('Valor digitado não e valido')

def pedir_categoria():
    while True:
        categoria = input('Digite a categoria da transação, de 2 a 30 caracteres: ')

        categoria = validacoes.validar_categoria(categoria)

        if categoria is not None:
            return categoria

        print('Categoria digitada não e valida')

def pedir_data():
    while True:
        data = input('Digite a data da transação (dd/mm/aaaa): ')

        data = validacoes.validar_data(data)

        if data is not None:
            return data

        print('Data digitada não e valida')

def pedir_id_existente():
    while True: 
        id = input('Digite o ID: ')

        id = validacoes.validar_id_existente(id)

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

def pedir_opcao():
    while True:
        a = input('Digite o numero opção desejada: ')
        a = validacoes.validar_opção(a)

        if a is not None: 
            return a

        print('valor digitado e invalido tente novamente')
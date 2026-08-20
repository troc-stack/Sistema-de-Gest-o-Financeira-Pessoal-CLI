from ui import terminal
from services import transacao

def main():

    while True:
        resp = terminal.menu()

        if resp == 1:
            print('Adicionar receita')
            Id = input('digite o id da receita')
            valor = int(input('Digite o valor: R$ '))
            categoria = input('digite a categoria da receita: ')
            data = input('digite a data: ')
            transacao.receita(Id, valor, categoria, data)

        elif resp == 2:
            print('Adicionar receita')
            Id = input('digite o id da receita')
            valor = int(input('Digite o valor: R$ '))
            categoria = input('digite a categoria da receita: ')
            data = input('digite a data: ')
            transacao.receita(Id, 'receita', valor, categoria, data)

        elif resp == 3: 
            print('Listar transações')
        elif resp == 4:
            print('Editar transação')
        elif resp == 5: 
            print('Excluir transação')
        elif resp == 6: 
            print('Buscar transação')
        elif resp == 7:
            print('Relatório financeiro')
        elif resp == 8: 
            print('Exportar dados')
        elif resp == 9:
            break

if __name__ == '__main__':
    main()
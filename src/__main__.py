from ui import terminal
from services import transacao
from services import GerenciadorTransacoes

def main():

    while True:
        resp = terminal.menu()

        if resp == 1:
            print('Adicionar Receita')

            Id = input('digite o id da receita')
            valor = int(input('Digite o valor: R$ '))
            categoria = input('digite a categoria da receita: ')
            data = input('digite a data: ')

            rr = transacao.Transacoes(Id, 'Receita', valor, categoria, data)
            rr.salvar_arquivo

        elif resp == 2:
            print('Adicionar Despesa')

            Id = input('digite o id da receita')
            valor = int(input('Digite o valor: R$ '))
            categoria = input('digite a categoria da receita: ')
            data = input('digite a data: ')
            
            dd = transacao.receita(Id, 'Despesa', valor, categoria, data)
            dd.salvar_arquivo 

        elif resp == 3: 
            gg = GerenciadorTransacoes.Gerenciador
            gg.listar

        elif resp == 4:
            gg = GerenciadorTransacoes.Gerenciador
            gg.listar

            id = input('informe o ID da trnasação que deseja editar')
            gg.buscar 
            



        elif resp == 5: 
            print('Excluir transação')

        elif resp == 6: 
            print('Buscar transação')
            gg = GerenciadorTransacoes.Gerenciador

            id = input('informe o ID da trnasação que deseja editar')
            gg.buscar

        elif resp == 7:
            print('Relatório financeiro')
        elif resp == 8: 
            print('Exportar dados')
        elif resp == 9:
            break

if __name__ == '__main__':
    main()
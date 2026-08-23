from ui import terminal
from services import transacao
from services import GerenciadorTransacoes

def main():

    while True:
        resp = terminal.menu()

        if resp == 1: #Adicionar receita
            print('Adicionar Receita')

            Id = int(input('digite o id da receita: '))
            valor =+ float(input('Digite o valor: R$ '))
            categoria = input('digite a categoria da receita: ')
            data = input('digite a data: ')

            rr = transacao.Transacoes(Id, 'Receita', valor, categoria, data)
            rr.salvar_arquivo()

        elif resp == 2: #Adicionar despesa
            print('Adicionar Despesa')

            Id = int(input('digite o id da receita: '))
            valor = -abs(float(input('Digite o valor: R$ ')))
            categoria = input('digite a categoria da receita: ')
            data = input('digite a data: ')
            
            rr = transacao.Transacoes(Id, 'Receita', valor, categoria, data)
            rr.salvar_arquivo()

        elif resp == 3: #Listar transações
            rr = GerenciadorTransacoes.Gerenciador()
            rr.listar()

        elif resp == 4: #Editar transação
            rr = GerenciadorTransacoes.Gerenciador()
            rr.listar()

            id = input('informe o ID da trnasação que deseja editar')
            rr.buscar(id)
            rr.editar(id) 

        elif resp == 5: #Excluir transação
            print('Excluir transação')

        elif resp == 6: #Buscar transação
            print('Buscar transação')
            rr = GerenciadorTransacoes.Gerenciador()

            id = input('informe o ID da trnasação: ')
            rr.buscar(id)

        elif resp == 7: #Relatório financeiro
            print('Relatório financeiro')

        elif resp == 8: #Exportar dados
            print('Exportar dados')
            
        elif resp == 9:
            break

if __name__ == '__main__':
    main()
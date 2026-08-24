from ui import terminal
from services import transacao
from services import GerenciadorTransacoes

def main():

    while True:
        resp = terminal.menu()

        if resp == 1: #Adicionar receita
            print('Adicionar Receita')

            Id = int(input('digite o id da receita: '))
            valor = +float(input('Digite o valor: R$ '))
            categoria = input('digite a categoria da receita: ')
            data = input('digite a data: ')

            rr = transacao.Transacoes(Id, 'Receita', valor, categoria, data)
            rr.salvar_arquivo()

        elif resp == 2: #Adicionar despesa
            print('Adicionar Despesa')

            Id = int(input('digite o id da receita: '))
            valor = -abs(float(input('Digite o valor: R$ ')))
            categoria = input('digite a categoria da Despesa: ')
            data = input('digite a data: ')
            
            rr = transacao.Transacoes(Id, 'Despesa', valor, categoria, data)
            rr.salvar_arquivo()

        elif resp == 3: #Listar transações
            rr = GerenciadorTransacoes.Gerenciador()
            rr.listar()

        elif resp == 4: #Editar transação
            rr = GerenciadorTransacoes.Gerenciador()
            rr.listar()

            id = int(input('informe o ID da tranasação que deseja editar'))
            rr.buscar(id)

            print('Oque deseja editar?')
            print('1 - ID  da transação; \n' \
            '2 - receita para despesa / despesa para receita; \n'\
            '3 - Valor\n' \
            '4 - Categoria\n'\
            '5 - Data\n' \
            '6 - cancelar')
            while True: 
                resp_ed = int(input('Escolha a opção de 1 a 5: '))
                if resp_ed == 1: 
                    chave = 'id'
                    novo = int(input('Informe o novo ID: '))
                    break 

                elif resp_ed == 2:
                    chave = 'tipo'
                    print('1 - Despesa\n' \
                    '2 - Receita')

                    while True:
                        tipo = int(input('Responda com 1 ou 2: '))
                        if tipo == 1: 
                            novo = 'Despesa'
                            break
                        elif tipo == 2:
                            novo = 'Receita'
                            break
                        elif tipo == 3:
                            print('cancelando')
                            resp_ed = 6
                            break
                        else: 
                            print('Valor informado incorreto:')
                    break

                elif resp_ed == 3: 
                    chave = 'valor'
                    novo = float(input('Digite o novo valor: '))
                    break 

                elif resp_ed == 4:
                    chave = 'categoria'
                    novo = input('Informe a nova descrição da transação: \n')
                    break 

                elif resp_ed == 5:
                    chave = 'data'
                    novo = input('informe a nova data: ')

                elif resp_ed == 6:
                    break

                else: 
                    print('opção invalida!!!')

            if resp_ed in [1,2,3,4,5]:
                rr.editar(id, chave, novo) 

        elif resp == 5: #Excluir transação
            print('Excluir transação')
            rr = GerenciadorTransacoes.Gerenciador()
            rr.listar()

            id = int(input('informe o ID da transação que deseja excluir'))
            rr.excluir(id)

        elif resp == 6: #Buscar transação
            print('Buscar transação')
            rr = GerenciadorTransacoes.Gerenciador()

            id = int(input('informe o ID da transação: '))
            rr.buscar(id)

        elif resp == 7: #Relatório financeiro
            print('Relatório financeiro')

        elif resp == 8: #Exportar dados
            print('Exportar dados')
            
        elif resp == 9:
            break

if __name__ == '__main__':
    main()
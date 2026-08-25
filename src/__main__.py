from ui import terminal
from services import transacao
from services import GerenciadorTransacoes
from utils import validacoes
from rich.traceback import install
install(show_locals=True)  

def main():

    while True:
        resp = terminal.menu()

        if resp == 1: #Adicionar receita
            print('Adicionar Receita')

            Id = validacoes.pedir_id()
            if Id is None:
                continue
            valor = validacoes.pedir_valor('Receita')
            categoria = validacoes.pedir_categoria()
            data = validacoes.pedir_data()

            rr = transacao.Transacoes(Id, 'Receita', valor, categoria, data)
            rr.salvar_arquivo()

        elif resp == 2: #Adicionar despesa
            print('Adicionar Despesa')

            Id = validacoes.pedir_id()
            if Id is None:
                continue
            valor = validacoes.pedir_valor('Despesa')
            categoria = validacoes.pedir_categoria()
            data = validacoes.pedir_data()
            
            rr = transacao.Transacoes(Id, 'Despesa', valor, categoria, data)
            rr.salvar_arquivo()

        elif resp == 3: #Listar transações
            rr = GerenciadorTransacoes.Gerenciador()
            if rr.existe_transacao() is False:
                continue
            rr.listar()

        elif resp == 4: #Editar transação
            rr = GerenciadorTransacoes.Gerenciador()
            if rr.existe_transacao() is False:
                continue

            rr.listar()

            id = validacoes.pedir_id_existente()
            if id is None:
                continue

            rr.buscar(id)

            print('Oque deseja editar?')
            print('1 - ID  da transação; \n' \
            '2 - receita para despesa ou mudar o valor; \n'\
            '3 - Categoria\n'\
            '4 - Data\n' \
            '5 - cancelar')
            while True: 
                resp_ed = int(input('Escolha a opção de 1 a 5: '))
                if resp_ed == 1: 
                    chave = 'id'
                    novo = validacoes.pedir_id()
                    break 

                elif resp_ed == 2:
                    chave = 'tipo'
                    print('1 - Despesa\n' \
                    '2 - Receita')

                    while True:
                        tipo = int(input('Responda com 1 ou 2: '))
                        if tipo == 1: 
                            novo = 'Despesa'
                            novo = validacoes.pedir_valor('Despesa')
                            break
                        elif tipo == 2:
                            novo = 'Receita'
                            novo = validacoes.pedir_valor('Receita')
                            break
                        elif tipo == 3:
                            print('cancelando')
                            resp_ed = 6
                            break
                        else: 
                            print('Valor informado incorreto:')
                    break

                elif resp_ed == 3:
                    chave = 'categoria'
                    categoria = validacoes.pedir_categoria()
                    break 

                elif resp_ed == 4:
                    chave = 'data'
                    data = validacoes.pedir_data()

                elif resp_ed == 5:
                    break

                else: 
                    print('opção invalida!!!')

            if resp_ed in [1,2,3,4]:
                rr.editar(id, chave, novo) 

        elif resp == 5: #Excluir transação
            print('Excluir transação')
            rr = GerenciadorTransacoes.Gerenciador()
            if rr.existe_transacao is False:
                print ('Não existe transação registrada')
                break
            rr.listar()
            
            id = validacoes.pedir_id_existente()
            if id is None:
                break

            rr = GerenciadorTransacoes.Gerenciador()
            rr.excluir(id)

        elif resp == 6: #Buscar transação
            print('Buscar transação')
            id = validacoes.pedir_id_existente()
            if id is None:
                break

            rr = GerenciadorTransacoes.Gerenciador()
            rr.buscar(id)

        elif resp == 7: #Relatório financeiro
            print('Relatório financeiro')

        elif resp == 8: #Exportar dados
            print('Exportar dados')
            
        elif resp == 9:
            break

if __name__ == '__main__':
    main()
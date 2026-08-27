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
                    if novo is None:
                        resp_ed = 5
                    break 

                elif resp_ed == 2:
                    chave = 'tipo'
                    print('1 - Despesa\n' \
                    '2 - Receita\n'\
                    '3 - Cancelar')

                    while True:
                        tipo = validacoes.pedir_opcao()
                        if tipo == 1:
                            chave = "tipo"
                            chave2 = "valor"
                            novo_modo = 'Despesa'
                            novo = validacoes.pedir_valor('Despesa')
                        
                        elif tipo == 2:
                            chave = "tipo"
                            chave2 = "valor"
                            novo_modo = 'Receita'
                            novo = validacoes.pedir_valor('Receita')
            
                        elif tipo == 3:
                            print('cancelando')
                            resp_ed = 6
                            break
                        else: 
                            print('Valor informado incorreto:')

                        rr.editar(id, chave, novo_modo) 
                        rr.editar(id, chave2, novo)
                        break

                elif resp_ed == 3:
                    chave = 'categoria'
                    novo = validacoes.pedir_categoria()
                    break 

                elif resp_ed == 4:
                    chave = 'data'
                    novo = validacoes.pedir_data()
                    break

                elif resp_ed == 5:
                    print('cancelando')
                    break

                else: 
                    print('opção invalida!!!')

            if resp_ed in [1,3,4]:
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
                continue

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
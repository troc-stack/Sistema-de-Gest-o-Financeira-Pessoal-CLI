import json

class Gerenciador:

    def __init__(self):
        try:
            with open("transacoes.json", "r", encoding="utf-8") as arquivo:
                self.__dados = json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            self.__dados = {"transações": []}

    def salvar_arquivo(self):
        with open('transacoes.json', 'w', encoding='utf-8') as a:
            json.dump(self.__dados, a, ensure_ascii=False, indent=4)

    def listar(self):

        print("--- LISTA DE TRANSAÇÕES ---")
        print('--' * 30)
        for elemento in self.__dados['transações']:
            print(f"| ID: {elemento['id']} "
                f"| Tipo: {elemento['tipo']} "
                f"| Valor: R$ {elemento['valor']:.2f} "
                f"| Categoria: {elemento['categoria']} "
                f"| Data: {elemento['data']}")
            print('--' * 30)

    def editar(self, id, chave, novo_valor):

        for elemento in self.__dados['transações']:
            if elemento['id'] == id:
                
                if chave in elemento:

                    elemento[chave] = novo_valor
                    self.salvar_arquivo()
                    
                    print(f"Campo '{chave}' atualizado com sucesso para: {novo_valor}")
                    return
                else:
                    print(f"Erro: A chave '{chave}' não existe na transação.")
                    return

        print("Transação não encontrada!")

    def excluir(self,id):

        for elemento in self.__dados['transações']:
            if elemento['id'] == id:
                self.__dados['transações'].remove(elemento)
                self.salvar_arquivo()
                print(f'transação de ID {id} foi excluida com sucesso!!!')
                return
        print('transação não encontrada')
        
    def buscar(self, id):
        for elemento in self.__dados['transações']:
            if elemento['id'] == id: 
                print('--' * 30)
                print(f"| ID: {elemento['id']} "
                    f"| Tipo: {elemento['tipo']} "
                    f"| Valor: R$ {elemento['valor']:.2f} "
                    f"| Categoria: {elemento['categoria']} "
                    f"| Data: {elemento['data']}")
                print('--' * 30)
                return
        print('transação não encontrada!!!')

    def id_transacao_existe(self, id):
        for elemento in self.__dados['transações']:
            if elemento['id'] == id:
                print('ID já existe')
                return True

        return False

    def existe_transacao(self):
        if not self.__dados["transações"]:
            print("Não há transações registradas.")
            return False

    def dados_relatorio(self):
            tabela_dados = [["ID", "Data", "Tipo", "Categoria", "Valor"]]
            total_receitas = 0 
            total_despesas = 0 

            for t in self.__dados['transações']:
                valor_formatado = f"R$ {t['valor']:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

                if t['tipo'] == 'Receita':
                    total_receitas += t['valor']
                else:
                    total_despesas += abs(t['valor'])
                
                tabela_dados.append([
                    str(t['id']),
                    str(t['data']),
                    str(t['tipo']),
                    str(t['categoria']).strip().capitalize(),
                    valor_formatado
                ])
            return tabela_dados, total_receitas, total_despesas
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
        if not self.__dados["transações"]:
            print("Não há transações registradas.")
            return

        n = 0 

        print("--- LISTA DE TRANSAÇÕES ---")
        for elemento in self.__dados['transações']:
            n += 1
            print('--' * 30)
            print(f'transação de número {n}')
            print('--' * 30)
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

                    if chave == 'valor':
                        novo_valor = float(novo_valor)

                    elemento[chave] = novo_valor
                    self.salvar_arquivo()
                    
                    print(f"Campo '{chave}' atualizado com sucesso para: {novo_valor}")
                    return
                else:
                    print(f"Erro: A chave '{chave}' não existe na transação.")
                    return

        print("Transação não encontrada!")

    def excluir(self,id):

        novos_dados = {"transações": []}

        for elemento in self.__dados['transaçõs']:
            if elemento['id'] == id:
                pass 
            else: 
                novos_dados['transações'].append(elemento)

        false = False
        for elemento in self.__dados['transaçõs']:
            if elemento['id'] == id:
                false = True    

        if false is False: 
            print('id não encontrado')

        self.__dados = novos_dados
        self.salvar_arquivo

    def buscar(self, id):
        for elemento in self.__dados['transaçõs']:
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

            
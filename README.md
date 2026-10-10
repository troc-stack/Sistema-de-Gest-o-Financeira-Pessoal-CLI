# Sistema de Gestão Financeira Pessoal CLI


## O que o sistema faz?
O usuário deve informar sobre suas transações (receitas e despesas) apresentando dados como:


* id
* Valor
* Categoria
* Data


Os dados fornecidos serão organizados e armazenados, a fim de posteriormente serem consultados pelo próprio usuário.


## porque ele existe?
O sistema foi criado no intuito de ajudar a acompanhar com clareza o que foi gasto e o que foi ganho em determinado período. Permitindo assim adquirir controle financeiro sobre as finanças.


Além disso, o sistema permite **criar e exportar um relatório financeiro em PDF**, salvando-o na pasta de downloads do dispositivo.


## Como executar?
Para executar o projeto, certifique-se de ter o Python instalado e execute o arquivo principal:


```bash
python -m src.__main__ 
```

## Como o código está organizado?
```bash
src/
├── services/
│   ├── gerenciador_transacoes.py
│   ├── relatorio.py
│   └── transacoes.py
├── ui/
│   └── terminal.py
└── utils/
    ├── entradas.py
    └── validacoes.py
```
## Lista de tarefas

[x] Cadastro e gerenciamento de receitas/despesas

[x] Validação de dados

[x] Criar e gerenciar os dados em .json 

[x] Geração e exportação de relatório em PDF

[ ] Refatoração e otimização do código

[ ] Melhorias na interface do usuário (HUD)

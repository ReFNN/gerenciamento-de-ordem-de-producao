# README - Sistema de Gerenciamento de Ordens de Produção

Este é um sistema de gerenciamento de ordens de produção para uma fábrica. Ele permite que você registre ordens de produção, liste as ordens existentes, verifique a disponibilidade de materiais, atualize o status das ordens e gere relatórios de produção.

## Requisitos Técnicos

- Linguagem de programação: Python
- Armazenamento de dados: SQLite (banco de dados)
- Interface: Linha de comando (CLI)

## Configuração

1. Clone este repositório para sua máquina:

```bash
git clone https://github.com/ReFNN/gerenciamento-de-ordem-de-producao
```

2. Certifique-se de que você tem o Python instalado em sua máquina.

3. Execute o arquivo `main.py` para iniciar o sistema.


## Como Usar

Após iniciar o sistema, você verá um menu com as seguintes opções:

1. Registrar nova ordem de produção
2. Listar todas as ordens de produção
3. Verificar disponibilidade de material
4. Atualizar status de uma ordem de produção
5. Visualizar relatórios de produção
6. Sair

## Exemplos de Entrada e Saída

Aqui estão alguns exemplos de entrada e saída para demonstrar o funcionamento do sistema:

### Exemplo 1 - Registrar Nova Ordem de Produção

- Escolha a opção 1 no menu.
- Digite o nome do produto: Vassoura
- Digite a quantidade desejada: 10
- Digite a data de entrega (DD-MM-YYYY): 15-10-2023
- A ordem de produção é registrada com sucesso.

### Exemplo 2 - Listar Todas as Ordens de Produção

- Escolha a opção 2 no menu.
- O sistema lista todas as ordens de produção existentes, mostrando detalhes de cada ordem, como o produto, a quantidade e a data de entrega.

### Exemplo 3 - Verificar Disponibilidade de Produção

- Essa opção falta ser implementada pois não entendi os requisitos nas instruções do desafio.

### Exemplo 4 - Atualizar Status de uma Ordem de Produção

- Escolha a opção 4 no menu.
- Digite o ID da ordem a ser atualizada: 1
- Digite o novo status (Em andamento/Concluída): Concluída
- O status da ordem é atualizado com sucesso.

### Exemplo 5 - Visualizar Relatórios de Produção

- Escolha a opção 5 no menu.
- O sistema mostra as ordens em andamento e as concluídas.




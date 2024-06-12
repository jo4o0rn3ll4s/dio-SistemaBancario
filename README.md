# Entendendo o Desafio

Neste projeto, você terá a oportunidade de aprimorar o Sistema Bancário em Python criado anteriormente. O objetivo é melhorar as três operações essenciais criadas: depósito, saque e extrato; Além de criar funções para cadastrar novos usuarios do banco e novas contas bancarias. O sistema será desenvolvido para um banco que busca monetizar suas operações. Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e demonstrar sua capacidade de desenvolver soluções práticas e eficientes.

#### Pré-requisitos:

- Lógica de Programação;

- Conhecimentos Básico(Python, Git, GitHub);

- Computador com SO de sua preferência(Windows, Linux, Mac OS);

- Ferramentas de Desenvolvimento (IDE)

# GitHub DIO - Trilha Python - Fundamentos

Todo código-fonte desenvolvido durante o projeto foi versionado no GitHub, no seguinte endereço:

https://github.com/digitalinnovationone/trilha-python-dio
 
https://www.dio.me

# Objetivo geral

Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

# Instruções adicionais

#### Funções de operações:

Para as operações temos algumas regras a serem aplicadas, sendo elas:

- Para saques:
```
A função saque deve receber os argumentos apelas por nome (keyword only).
- Sugestões de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
- Sugestão de retorno: saldo e extrato.
```

- Para depositos:
```
A função deposito deve recever os argumentos apenas por posição (positional only).
- Sugestão de argumentos: saldo, valor, extrato.
- Sugestão de retorno: saldo e extrato.
```

- Para extrato:
```
A função extrato deve receber os argumentos por posição e nome (posicional only e keyword only).
- Argumentos posicionais: saldo.
- Argumentos nomeados: extrato.
```

#### Funções de cadastro:

- Criar usuário (cliente):
```
O programa deve armazenar os usuários em uma lista, um usuário é composto por:
    1. Nome
    2. Data De Nascimento
    3. CPF
    4. Endereço

* não pode haver 2 cadastros de usuários com o mesmo CPF *
```

- Criar conta bancaria:
```
O programa deve armazenar contas em uma lista, uma conta é composta por:
    1. Agência
    2. Número Da Conta
    3. Usuário

O número da conta é sequencial, iniciando em 1.
O número da agência é fixo: "0001".
O usúario pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
```

**Bons estudos**

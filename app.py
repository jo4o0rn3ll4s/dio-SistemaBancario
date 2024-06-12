import json

COR = {
    'limpa': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

################################################################
#Funções auxiliares:                                           #
#   Para o usuario:                                            #
#   -carregar_usuarios() -> dict                               #
#   -atualizar_usuarios() -> bool                              #
#   Para a conta:                                              #
#   -carregar_contas() -> dict                                 #
#   -atualizar_contas() -> bool                                #
################################################################

# importa os usuarios do banco
def carregar_usuarios() -> dict:
    '''
    Carrega os usuarios do banco de dados.
    \n
    Return: o objeto 'users' com as informações.
    '''
    try:
        with open('db/users.json', 'r',encoding='UTF-8') as file:
            users = json.load(file)
    except:
        print('Arquivo não encontrado, criando um...')
        users = {}
    return users
def atualizar_usuarios(obj) -> bool:
    '''
    Atualiza o arquivo '.json' com o objeto passado.
    \n
    Argumentos: o objeto 'users' com as informações.
    \n
    Return: True se o arquivo foi atualizado com sucesso, ou False caso haja algum problema.
    '''
    try:
        users = carregar_usuarios()
        users.update(obj)
        with open('db/users.json', 'w', encoding='UTF-8') as file:
            json.dump(users, file, indent=4, ensure_ascii=False)
        return True
    except:
        print('Ocorreu um erro inesperado, tente novamente')
        return False


# importa as contas do banco
def carregar_contas() -> dict:
    '''
    Carrega as contas bancarias armazenadas no json.
    \n
    Return: o objeto 'account' com as informações.
    '''
    try:
        with open('db/accounts.json', 'r',encoding='UTF-8') as file:
            account = json.load(file)
    except:
        print('Arquivo não encontrado, criando um...')
        account = {}
    return account
def atualizar_contas(obj) -> bool:
    '''
    Atualiza o arquivo '.json' com o objeto passado.
    \n
    Argumentos: o objeto 'account' com as informações.
    \n 
    Return: True se o arquivo foi atualizado com sucesso, ou False caso haja algum problema.
    '''
    try:
        accounts = carregar_contas()
        accounts.update(obj)
        with open('db/accounts.json', 'w', encoding='UTF-8') as file:
            json.dump(accounts, file, indent=4, ensure_ascii=False)
        return True
    except:
        print('Ocorreu um erro inesperado, tente novamente')
        return False


################################################################
#Funções principais:                                           #
#   cadastros:                                                 #
#   -cadastrar_usuario()                                       #
#   -cadastrar_conta()                                         #
#   operações:                                                 #
#   -sacar()                                                   #
#   -depositar()                                               #
#   -mostrar_saldo()                                           #
#   -mostrar_extrato()                                         #
################################################################

# cria um usuario para cadastrar no banco
def cadastrar_usuario():
    '''
    Cadastra um novo usuario no sistema.
    \n
    Sem argumentos, e sem retorno.
    '''
    users = carregar_usuarios()
    print('Iniciar cadastro:')
    
    cpf = input("Digite o cpf do titular: ")
    for i in range(1,len(users)+1):
        if users[str(i)]['dados']['cpf'] == cpf:
            print('Cadastro já existente!')
            return
    nome = input("Digite o nome do titular: ")
    nasc = input("Digite a data de nascimento do titular: ")
    end = input("Digite o endereço do titular: ")
        
    id = len(users)+1
    cadastro = {
        id: {
        'dados':{
            'nome': nome,
            'nascimento': nasc,
            'cpf': cpf,
            'endereço': end
        },
        'contas' : []
        }
    }
    
    atualizar_usuarios(cadastro)

# cria uma conta bancaria no sistema
def cadastrar_conta():
    '''
    Cadastra uma nova conta no sistema.
    \n
    Sem argumentos, e sem retorno.
    '''
    tipo_conta = {
        '1':{
            'tipo': 'corrente',
            'saque_diario': 9999,
            'saque_maximo': 1000
            },
        '2':{
            'tipo': 'salario',
            'saque_diario': 3,
            'saque_maximo': 10000
            },
        '3':{
            'tipo': 'poupança',
            'saque_diario': 3,
            'saque_maximo': 500
            }
        }
    
    users = carregar_usuarios()
    
    cpf = input('Digite o CPF do titular: ')
    i = 1
    while i <= len(users):
        if users[str(i)]['dados']['cpf'] == cpf:
            print('Abrindo conta:')
            senha = input("Digite uma senha para uso nas transações (4 digitos): ")
            
            rpt = True
            while rpt:
                tipo = input('''
Qual tipo de conta deseja abrir? 

[1] - Corrente
[2] - Salario
[3] - Poupança
=> ''')

                if tipo in tipo_conta.keys():
                    print('Informações sobre a conta corrente:')
                    db_contas = carregar_contas()
                    n_conta = len(db_contas)+1
                    
                    conta = {
                        n_conta : {
                        'tipo': tipo_conta[tipo]['tipo'],
                        'agc': '0001',
                        'numero_da_conta': n_conta,
                        'senha': senha,
                        'saldo': 0,
                        'saque_diario': tipo_conta[tipo]['saque_diario'],
                        'saque_maximo': tipo_conta[tipo]['saque_maximo'],
                        'historico': []
                        }
                    }
                    print(conta)
                    
                    atualizar_contas(conta)
                    print(f'Conta nº {n_conta} criada com sucesso!')
                    
                    users[str(i)]['contas'].append(n_conta)
                    atualizar_usuarios(users)
                    print(f"Conta vinculada ao titular de CPF {users[str(i)]['dados']['cpf']}")
                    
                    rpt = False
                else:
                    print('Digite uma opção valida de conta')
        i += 1
    else:
        print('CPF não encontrado.\nPara abrir uma conta no Banco DioPy primeiro crie um cadastro conosco.')

    
# realiza a operação de saque em uma conta
def sacar(*,n_conta, valor):
    '''
    Função que realiza o saque em uma conta.
    \n
    Argumentos:
    \n\tn_conta: numero da conta para ser encontrada e realizada suas operações mediante senha pessoal.
    \n\tvalor: valor que deseja realizar o saque.
    '''
    contas = carregar_contas()
    for i in range(1,len(contas)+1):
        if contas[str(i)]['numero_da_conta'] == int(n_conta):
            senha = input("Digite sua senha para operações: ")
            if valor <= contas[str(i)]["saldo"] and valor <= contas[str(i)]["saque_maximo"] and  contas[str(i)]["saque_diario"] != 0 and senha == contas[str(i)]["senha"]:
                contas[str(i)]["saldo"] -= valor
                contas[str(i)]["saque_diario"] -= 1
                contas[str(i)]['historico'].append(f'{COR['vermelho']}-{valor:.2f}{COR['limpa']}')
                print(f'Saque de R${valor:.2f} realizado')
                atualizar_contas(contas)
                return
            else:
                print('Erro ao realizar saque.')
    else:
        print("Conta não encontrada!")

# realiza a operação de depositar numa conta
def depositar(n_conta, valor,/):
    '''
    Função que realiza o saque em uma conta.
    \n
    Argumentos:
    \n\tn_conta: numero da conta para ser encontrada.
    \n\tvalor: valor que deseja realizar o deposito.
    '''
    contas = carregar_contas()
    for i in range(1,len(contas)+1):
        if contas[str(i)]['numero_da_conta'] == int(n_conta):
            contas[str(i)]["saldo"] += valor
            contas[str(i)]['historico'].append(f'{COR['verde']}+{valor:.2f}{COR['limpa']}')
            print(f'Deposito no valor de R${valor:.2f} realizado')
            atualizar_contas(contas)
            return
    else:
        print("Conta não encontrada!")

#realiza a operação de apresetar o saldo bancario
def mostrar_saldo(n_conta):
    contas = carregar_contas()
    for i in range(1,len(contas)+1):
        if contas[str(i)]['numero_da_conta'] == int(n_conta):
            print(f'Saldo atual na conta: R${contas[str(i)]['saldo']}')
            return
    else:
        print('Conta não encontrada!')

# realiza a operação de apresentar o extrato bancario
def mostrar_extrato(n_conta):
    contas = carregar_contas()
    for i in range(1,len(contas)+1):
        if contas[str(i)]['numero_da_conta'] == int(n_conta):
            print(f'Saldo atual na conta: R${contas[str(i)]["saldo"]}')
            print(f'Extrato da conta: ')
            for j in range(len(contas[str(i)]['historico'])):
                print(f'[{j+1}] - {contas[str(i)]['historico'][j]}')
            return
    else:
        print('Conta não encontrada!')

import json

################################################################
#Funções auxiliares:                                           #
#   Para o usuario:                                            #
#   -carregar_usuarios() -> dict                               #
#   -atualizar_usuarios(obj) -> bool                           #
#   Para a conta:                                              #
#   -carregar_contas() -> dict                                 #
#   -atualizar_contas(obj) -> bool                             #
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
        print('Arquivo de usuario não encontrado, criando um...')
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

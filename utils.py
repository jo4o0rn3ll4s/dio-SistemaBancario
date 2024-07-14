from models import *
from time import sleep
import os

# region - Constantes
CONFIRMA = ('S','SIM','SS')

COR = {
    'limpa': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}
# endregion

def limpar(tempo: int = 2) -> None:
    sleep(tempo)
    os.system('cls')

def retornar_perfil(cpf) -> dict | str | bool:
    users = carregar_usuarios()
    for i in range(1,len(users)+1):
        if users[str(i)]["cpf"] == cpf:
            return users[str(i)], str(i), True
    else:
        return None, None, False

def retornar_conta(n_conta) -> dict | bool:
    accounts = carregar_contas()
    for i in range(1,len(accounts)+1):
        if accounts[str(i)]['numero'] == n_conta:
            return accounts[str(i)], True
    else:
        return None, False

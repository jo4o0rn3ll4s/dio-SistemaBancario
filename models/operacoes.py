from models.app import *
import abc

COR = {
    'limpa': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

class Transacao(abc.ABC):
    def __init__(self):
      pass

    @abc.abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor
    def registrar(self, conta) -> bool:
        accounts = carregar_contas()
        conta = conta.__dict__
        for i in range(1,len(accounts)+1):
            if accounts[str(i)]["numero"] == conta["numero"]:
                accounts[str(i)]["saldo"] += self._valor
                accounts[str(i)]["historico"].append(f'{COR['verde']}+{self._valor}{COR['limpa']}')
                return atualizar_contas(accounts)
        else:
            print("Conta não encontrada!")
            return False

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    def registrar(self, conta):
        accounts = carregar_contas()
        conta = conta.__dict__
        for i in range(1,len(accounts)+1):
            if accounts[str(i)]["numero"] == conta["numero"]:
                accounts[str(i)]["saldo"] -= self._valor
                accounts[str(i)]["historico"].append(f'{COR['vermelho']}-{self._valor}{COR['limpa']}')
                return atualizar_contas(accounts)
        else:
            print("Conta não encontrada!")
            return False

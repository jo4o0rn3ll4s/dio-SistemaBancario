from models.operacoes import Deposito, Saque
from models.cliente import Cliente

from models.app import *
from utils import *

class Conta:
    def __init__(self, saldo:float, numero:str, agencia:int, cliente:dict,
    senha: str,historico:list=[]):
      self.saldo = saldo
      self.numero = numero
      self.agencia = agencia
      self.cliente = cliente
      self.senha = senha
      self.historico = historico
    
    def __str__(self) -> str:
        return f"""
Informações:
\t{'\n\t'.join([f"{i}: {j}" for i,j in self.__dict__.items()])}
"""

    def mostrar_saldo(self) -> bool | float:
        account, state = retornar_conta(self.numero)
        return state, account["saldo"] if state else 0
    
    def nova_conta(self, cliente: Cliente) -> bool | bool:
        """Return-> atualização de users, account"""
        users = carregar_usuarios()
        account = carregar_contas()
        
        cliente = cliente.__dict__
    
        for i in range(1,len(users)+1):
            if users[str(i)]['cpf'] == cliente['cpf']:
                for j in range(len(users[str(i)]['contas'])):
                    if users[str(i)]['contas'][j]['numero'] == self.numero:
                        print(f'Conta {self.numero} já existente.')
                        return False, False
                else:
                    users[str(i)]['contas'].append({'numero': self.numero})
                    account.update({self.numero:self.__dict__})
                    return atualizar_usuarios(users), atualizar_contas(account)
        else:
            print(f'Usuario do cpf:{cliente['cpf']} não encontrado.')
            return False, False
    
    def sacar(self, valor:float) -> bool:
        item = Saque(valor)
        if item.registrar(self):
            self.historico.append(f'{COR['vermelho']}-{valor}{COR['limpa']}')
            return True
        else:
            return False
        
    def depositar(self, valor:float) -> bool:
        item = Deposito(valor)
        if item.registrar(self):
            self.historico.append(f'{COR['verde']}+{valor}{COR['limpa']}')
            return True
        else:
            return False

class Conta_Corrente(Conta):
    def __init__(self, saldo:float, numero:str, agencia:str, cliente: dict,
    senha:str,
    historico:list=[], limite:float=1000.0, limite_saque: int=9999):
        super().__init__(saldo= saldo, numero=numero, agencia=agencia, cliente=cliente, senha=senha, historico= historico)
        self.limite = limite
        self.limite_saque = limite_saque
    
class Conta_Poupanca(Conta):
    def __init__(self, saldo:float, numero:str, agencia:str, cliente:dict,
    senha: str,
    historico:list=[], limite:float=500.0, limite_saque: int=3):
        super().__init__(saldo= saldo, numero=numero, agencia=agencia, cliente=cliente, senha=senha, historico= historico)
        self.limite = limite
        self.limite_saque = limite_saque

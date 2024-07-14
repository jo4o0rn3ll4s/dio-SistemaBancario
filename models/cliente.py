#from models.operacoes import Saque, Deposito

from models.app import *
from datetime import datetime

class Pessoa_Fisica:
    def __init__(self, cpf:str, nome:str, data_nascimento:datetime):
      self.cpf = cpf
      self.nome = nome
      self.data_nascimento = data_nascimento
    
    def __str__(self):
        return f"""
classe: {self.__class__.__name__}
informações:
    {'\n'.join([f'{i}: {j}' for i,j in self.__dict__.items()])}
"""

class Cliente(Pessoa_Fisica):
    def __init__(self, cpf:str, nome:str, data_nascimento:datetime,endereco:str,contas:list = []):
        super().__init__( cpf, nome, data_nascimento)
        self.endereco = endereco
        self.contas = contas

    def __str__(self):
        return f"""
classe: {self.__class__.__name__}
informações:
\t{'\n\t'.join([f'{i}: {j}' for i,j in self.__dict__.items()])}
"""

    '''
    def realizar_transacao(self,conta,transacao):
        pass
    '''
    
    def adicionar_cliente(self) -> bool:
        users = carregar_usuarios()
        client = self.__dict__
        for i in range(1,len(users)+1):
            if users[str(i)]['cpf'] == client['cpf']:
                print(f'O usuario de cpf {client["cpf"]} já está cadastrado no sistema!')
                return False
        else:
            users.update({len(users)+1:client})
            return atualizar_usuarios(users)


''' # implementar #
class Funcionario(Pessoa_Fisica):
    def __init__(self, cpf:str, nome:str, data_nascimento:datetime,cargo:str):
        super().__init__( cpf, nome, data_nascimento)
        self.cargo = cargo
'''
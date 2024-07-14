#from models import *
from utils import  *

abertura = f"""
-BANCO DIOPY-

[1] - Acessar perfil
[2] - Criar perfil
[3] - Acessar conta
[4] - Criar conta

[5] - Sair
"""
menu = f"""
-BANCO DIOPY-

[1] - Depositar
[2] - Sacar
[3] - Saldo
[4] - Extrato

[5] - Sair

"""
menu_contas = f"""
-BANCO DIOPY-

[1] - Corrente
[2] - Poupança

"""

def tela_0():
    while True:
        print(abertura)
        escolha = input('Escolha a operação: ')
        
        # Sair do Sistema
        if escolha == "5":
            print("Saindo...")
            limpar()
            break
        
        # Acessar perfil
        if escolha == "1":
            cpf = input('Digite o cpf do usuario: ')
            
            match, _, valida = retornar_perfil(cpf)
            
            if valida:
                if len(match['contas']) > 0:
                    print(f'{"CONTAS":-^15}')
                    for j in range(len(match["contas"])):
                        print(f'{j+1} - conta numero: {match["contas"][j]["numero"]}')
                    
                    escolha_conta = input('Digite que conta deseja entrar -> ')
                    
                    while int(escolha_conta)-1 not in list(range(len(match["contas"]))):
                        print("Escolha invalida! Tente novamente")
                        limpar()
                        for j in range(len(match["contas"])):
                            print(f'{j+1} - conta numero: {match["contas"][j]["numero"]}')
                    
                        escolha_conta = input('Digite que conta deseja entrar -> ')
                    
                    print(menu_contas)
                    tipo = input('Qual tipo de conta -> ')
                    
                    conta, valida = retornar_conta(match["contas"][int(escolha_conta)-1]['numero'])
                    if valida:
                    
                        if tipo == '1':
                            obj = Conta_Corrente(**conta)
                        elif tipo == '2':
                            obj = Conta_Poupanca(**conta)
                    
                        tela_1(obj)
                    
                    else:
                        print('Conta não encontrada! tente novamente outra vez')
                        limpar()
                else:
                    print('Este usuario não possui contas.')
                    limpar()
            else:
                print("Usuário não encontrado!")
                limpar()
        
        # Criar perfil
        if escolha == "2":
            cpf = input('Digite o cpf do usuario: ')
            
            if ((retornar_perfil(cpf))[2]):
                print(f'O cpf {cpf} já está cadastrado no sistema do banco.')
            
            else:
                while True:
                    nome = input('Digite o nome do usuario: ')
                    nasc = input('Digite a data de nascimento (dd/mm/yyyy): ')
                    end = input('Digite o endereço do usuario: ')
                    
                    cliente = Cliente(cpf=cpf,nome=nome, data_nascimento=nasc, endereco=end)
                    
                    print(cliente)
                    confirma = input('Confirma os dados? S | N -> ').upper()
                    if confirma in CONFIRMA:
                        if cliente.adicionar_cliente():
                            print('Cliente adicionado com sucesso')
                        else:
                            print('Ocorreu um erro inesperado, tente novamente mais tarde.')
                            limpar()
                        break
                    else:
                        print('Entendido, tente outra vez')
                        limpar()
             
        # Acessar conta
        if escolha == "3":
            print(menu_contas)
            esco = input('Qual tipo de conta -> ')
            
            n_conta = str(input('Digite o numero da conta: '))
            match, valida = retornar_conta(n_conta)
            
            if valida:
                if esco == '1':
                    obj = Conta_Corrente(**match)
                elif esco == '2':
                     obj = Conta_Poupanca(**match)
                
                obj_dct = obj.__dict__
                
                senha = input("Digite sua senha: ")
                x = 5
                while senha != obj_dct["senha"]:
                    print(f"Senha incorreta! Tente outra vez, em {x} tentativas a conta será bloqueada")
                    if x > 0:
                        x-=1
                    else:
                        print("Você excedeu o numero de tentativas de inserção da senha! Tente outra hora.")
                        break
                    senha = input("Digite sua senha: ")
                
                if x != 0:
                    limpar()
                    tela_1(obj)
                     
            else:
                print("Usuário não encontrado!")
                limpar()

        # Criar conta
        if escolha == "4":
            esco = input("Já possui cadastro em nosso banco? S | N -> ").upper()
            
            if esco in CONFIRMA:
                cpf = input('Digite o cpf do usuario: ')
                
                match, id, valida = retornar_perfil(cpf)
                
                if valida:
                    while True:
                        print(menu_contas)
                        esco_conta = input('Qual tipo de conta -> ')
                        esco_saldo = input("Deseja fazer um depósito inicial? S | N -> ").upper()
                        if esco_saldo in CONFIRMA:
                            saldo = float(input('Digite o valor que deseja depositar: R$'))
                        else:
                            saldo = 0
                            print('Okay... sigamos então.')

                        senha = input('Digite sua senha de 4 digitos: ')
                                            
                        if esco_conta == "1":
                            conta = Conta_Corrente(saldo=saldo,numero=str(len(carregar_contas())+1),agencia='0001',cliente={"id": id,"nome":match["nome"]},senha=senha)
                        elif esco_conta == "2":
                            conta = Conta_Poupanca(saldo=saldo,numero=str(len(carregar_contas())+1),agencia='0001',cliente={"id": id,"nome":match["nome"]},senha=senha)
                        
                        print(conta)
                        confirma = input('Confirma os dados? S | N -> ').upper()
                        if confirma in CONFIRMA:
                            if conta.nova_conta(Cliente(**match)):
                                print('Conta criada com sucesso')
                                limpar()
                            else:
                                print('Ocorreu um erro inesperado, tente novamente mais tarde.')
                                limpar()
                            break
                        else:
                            print('Entendido, tente outra vez')
                            limpar()
                else:
                    print('ERRO! Cpf não encontrado em nosso sistema!')
                    limpar()
            else:
                print('Crie um cadastro conosco antes de abrir sua conta.')
                limpar()
        
        else:
            print("Opção inválida!")
            limpar()

def tela_1(obj_conta):
    while True:
        
        print(menu)
        escolha = input('Escolha a operação: ')
        
        # Sair da Conta
        if escolha == "5":
            print("Saindo...")
            limpar()
            break
        
        # Depositar
        elif escolha == "1":
            dep = obj_conta.depositar(int(input("Digite o valor a ser depositado -> R$ ")))
            if dep and atualizar_contas(obj_conta):
                print("Deposito realizado com sucesso")
            else:
                print("Ocorreu um erro ao Realizar o depósito...\nTente novamente mais tarde")

        # Sacar
        elif escolha == "2":
            sac = obj_conta.sacar(int(input("Digite o valor a ser sacado -> R$ ")))
            if sac and atualizar_contas(obj_conta):
                print("Saque realizado com sucesso")
            else:
                print("Ocorreu um erro ao Realizar o saque...\nTente novamente mais tarde")
        
        # Mostar saldo
        elif escolha == "3":
            state, saldo = obj_conta.mostrar_saldo()
            if state:
                print(f'O saldo em conta é de R$ {saldo}')
            else:
                print("Ocorreu um erro inesperado, tente novamente mais tarde")
            input("Precione ENTER para seguir... ")
            limpar()
        
        # Exibir extrato
        elif escolha == "4":
            print(f"{'EXTRATO':-^15}")
            for i in range(len(obj_conta.__dict__["historico"])):
                print(f"{i+1} - {obj_conta.__dict__['histórico'][i]}")
            input("Precione ENTER para seguir... ")
            limpar()
            
        else:
            print('Operação inexistente.\nPor favor, digite uma opção valida!')
            limpar()

if __name__ == "__main__":
    tela_0()

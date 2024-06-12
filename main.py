from time import sleep
import os
import app


abertura = f"""
BANCO DIOPY

[1] - Acessar perfil
[2] - Criar perfil
[3] - Acessar conta
[4] - Criar conta

[5] - Sair
"""

menu = f"""
BANCO DIOPY

[1] - Depositar
[2] - Sacar
[3] - Saldo
[4] - Extrato

[5] - Sair

"""


def tela0():
    while True:
        print(abertura)
        escolha = input('Escolha a operação: ')
        
        if escolha == "5":
            os.system('cls')
            print("Saindo...")
            sleep(2)
            break
        
        elif escolha == "1":
            
            # função acessar perfil
            users = app.carregar_usuarios()
            cpf = input('Digite o CPF do titular para acessar suas contas: ')
            i = 1
            while i <= len(users):
                if users[str(i)]['dados']['cpf'] == cpf:
                    if len(users[str(i)]['contas']) > 0:
                        print("Suas contas são: ")
                        
                        for j in range(len(users[str(i)]['contas'])):
                            print(f'[{j+1}] - {users[str(i)]['contas'][j]}')
                            
                        conta = input('Digite a conta que deseja realizar as operações: ')
                        tela1(conta)
                        
                        break
                    else:
                        print('Você não possui contas ainda, crie uma caso queira utilizar nossos serviços.')
                i += 1
            else:
                print('Conta não encontrada!')
                    
            sleep(2)
            os.system('cls')
            
        elif escolha == "2":
            
            # função criar perfil
            app.cadastrar_usuario()
            
            sleep(2)
            os.system('cls')
            
        elif escolha == "3":
            
            # função acessar conta
            contas = app.carregar_contas()
            n_conta = input('Digite o nº da conta que deseja acessar: ')
            for i in n_conta:
                if i == n_conta:
                    tela1(n_conta)
                    break
            else:
                print('Conta não encontrada!')
                
            sleep(2)
            os.system('cls')
            
        elif escolha == "4":
            
            # função criar conta
            app.cadastrar_conta()
            
            sleep(2)
            os.system('cls')
              
        else:
            print('Opção inválida!')
            sleep(2)
            os.system('cls')

def tela1(n_conta):
    while True:
        
        print(menu)
        escolha = input('Escolha a operação: ')
        
        if escolha == "5":
            os.system('cls')
            print("Saindo...")
            sleep(2)
            break
        
        elif escolha == "1":
            
            # função depositar
            valor = input('Quanto irá depositar?: ')
            app.depositar(n_conta, float(valor))
            
            sleep(2)
            os.system('cls')
            
        elif escolha == "2":
            
            # função sacar
            valor = input('Quanto deseja sacar?: ')
            app.sacar(n_conta=n_conta, valor=float(valor))
            
            sleep(2)
            os.system('cls')
            
        elif escolha == "3":
            
            # função saldo
            app.mostrar_saldo(n_conta)
            
            sleep(2)
            os.system('cls')
            
        elif escolha == "4":
            
            # função extrato
            app.mostrar_extrato(n_conta)
            
            input('Tecle "enter" para prosseguir...')
            os.system('cls')
            
        else:
            print('Operação inexistente.\nPor favor, digite uma opção valida!')
            sleep(2)
            os.system('cls')

if __name__ == "__main__":
    tela0()

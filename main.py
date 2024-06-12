from time import sleep
import os

operacoes = list()
conta = 500.00

SAQUE_DIARIO = 3
SAQUE_MAXIMO = 500
COR = {
    'limpa': '\033[m',
    'verde': '\033[32m',
    'vermelho': '\033[31m'
}

menu = f"""
BANCO DIOPY

[1] - Depositar
[2] - Sacar
[3] - Saldo
[4] - Extrato

[5] - Sair

"""

while True:
    
    print(menu)
    escolha = input('Escolha a operação: ')
    
    if escolha == "5":
        os.system('cls')
        print("Saindo...")
        sleep(2)
        break
    
    elif escolha == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        
        conta += valor
        print(f'Foi depositado R${valor:.2f} na conta.')
        operacoes.append(f'{COR["verde"]}+R${valor:.2f}{COR['limpa']}')
        
        sleep(2)
        os.system('cls')
        
    elif escolha == "2":
        if SAQUE_DIARIO > 0:
            rpt = True
            while rpt:    
                valor = float(input("Digite o valor a ser sacado: "))
                
                if valor <= 500:
                    conta -= valor
                    print(f'Foi sacado R${valor:.2f} da conta.')
                    SAQUE_DIARIO -= 1
                    operacoes.append(f'{COR["vermelho"]}-R${valor:.2f}{COR["limpa"]}')
                    rpt = False
                else:
                    print('O valor excede o limite de saque. Realize um saque de menor valor.')
                    rpt = True
        
        else:
            print('Limite de saques diarios atingido. Por favor, tente outro dia.')
            
        sleep(2)
        os.system('cls')
        
    elif escolha == "3":
        print(f'Saldo atual: R${conta:.2f}')
        
        sleep(2)
        os.system('cls')
        
    elif escolha == "4":
        print('Ultimas operações: ')
        
        for i in range(len(operacoes)):
            print(f'[{i+1}] - {operacoes[i]}')
        
        input('Tecle "enter" para prosseguir...')
        os.system('cls')
        
    else:
        print('Operação inexistente.\nPor favor, digite uma opção valida!')
        sleep(2)
        os.system('cls')


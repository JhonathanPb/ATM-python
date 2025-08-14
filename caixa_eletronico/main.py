import time
from funcoes_banco import operacoes

contas = operacoes.carregar_dados()

while True:
    operacoes.limpar_tela()
    print('-----------------')
    print('---ATM PY BANK---')
    print('1. Login')
    print('2. Sair')
    print('-----------------')
    
    opcoes_menu = input('DIGITE UMA OPÇÃO: ')
    
  
    if opcoes_menu == '1':
        print('Digite sua Conta e Senha')
        conta = input('Conta: ')
        senha = input('Senha: ')
        
        print(f"DEBUG: A conta digitada é: {conta}")
        print(f"DEBUG: A senha digitada é: {senha}")
        
        time.sleep(2)
        
        if operacoes.verificar_dados(contas, conta, senha):
            while True:
                print('Login efetuado com sucesso:')
                operacoes.limpar_tela()
                
                print('-----------------')
                print('---ATM PY BANK---')
                print(f'Olá, conta {conta}!')
                print('1. Sacar')
                print('2. Depositar')
                print('3. Verificar Saldo') 
                print('4. Sair')
                print('-----------------')
                
                operacoes_bancarias = input('DIGITE UMA OPÇÃO: ') 
                
                if operacoes_bancarias == '1':
                    pass
                
                elif operacoes_bancarias == '2':
                    pass
                
                elif operacoes_bancarias == '3':
                    pass
                
                elif operacoes_bancarias == '4':
                    print('Obrigado por usar ATM PY BANK')
                    break
                
                else:
                    print('Opção INVÁLIDA!!')
                      
        else:
            print('Usuario ou senha incorretos!')
            operacoes.limpar_tela()
            time.sleep(3)
            print('Voltando para o menu inicial em....')
            time.sleep(3)
            print('3')
            time.sleep(2)
            print('2')
            time.sleep(2)
            print('1')
            time.sleep(2)
            
    elif opcoes_menu == '2':
        print('Obrigado por Usar o ATM PY BANK!')
        break
    
    else:
        print('Opção INVÁLIDA.')

        

    
        
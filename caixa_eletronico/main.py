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
        print('Digite sua Conta')
        conta = input('Conta: ')
        
        if conta in contas:
            nome_usuario = contas[conta]['nome']
            print(f'Bem-Vindo, {nome_usuario}!')
            
            time.sleep(3)
            
            print('Digite sua Senha')
            senha = input('Senha: ')
            
            time.sleep(3)
            
            if operacoes.verificar_dados(contas, conta, senha):
                operacoes.limpar_tela()
                
                while True:
                    print('Login efetuado com sucesso')
                    time.sleep(3)
                    operacoes.limpar_tela()
                    
                    print('-----------------')
                    print('---ATM PY BANK---')
                    print(f'Olá, conta {nome_usuario}!')
                    print('1. Sacar')
                    print('2. Depositar')
                    print('3. Verificar Saldo') 
                    print('4. Sair')
                    print('-----------------')
                    
                    operacoes_bancarias = input('DIGITE UMA OPÇÃO: ') 
                    
                    if operacoes_bancarias == '1':
                        print('Digite o valor que deseja sacar')
                        valor = int(input('Valor: '))
                        
                        valor = operacoes.sacar(contas, conta, valor)
                        if valor is not None:
                            print(f'Saque realizado com sucesso! Valor sacado: R${valor}')
                            valor = contas[conta]['saldo']
                        
                        else:
                            print('Saldo insuficiente ou valor inválido para saque.')
                    
                    elif operacoes_bancarias == '2':
                        pass
                    
                    elif operacoes_bancarias == '3':
                        pass
                    
                    elif operacoes_bancarias == '4':
                        print('Voltando ao Menu inicial')
                        time.sleep(3)
                        break
                    
                    else:
                        print('Opção INVÁLIDA!!')
                        
            else:
                operacoes.limpar_tela()
                print('Senha incorretos!')
                time.sleep(3)
                operacoes.limpar_tela()
                print('Voltando para o menu inicial em....')
                time.sleep(3)
                print('3')
                time.sleep(2)
                print('2')
                time.sleep(2)
                print('1')
                time.sleep(2)
        else:
            print('Conta não encontrada!')
            time.sleep(3)
            

            
    elif opcoes_menu == '2':
        print('Obrigado por Usar o ATM PY BANK!')
        break
    
    else:
        print('Opção INVÁLIDA.')

        

    
        
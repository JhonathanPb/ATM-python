from funcoes_banco import operacoes

operacoes.carregar_dados()

while True:
    operacoes.limpar_tela()
    print('-----------------')
    print('---ATM PY BANK---')
    print('1. Login')
    print('2. Sair')
    print('-----------------')
    
    opcoes = input('DIGITE UMA OPÇÃO: ')
    
  
    if opcoes == '1':
        print('Digite sua Conta e Senha')
        conta = input('Conta: ')
        senha = input('Senha: ')
        
        if operacoes.verificar_dados(conta, senha):
            print('Login efetuado com sucesso:')
            
            operacoes.limpar_tela()
            
            print('1. Sacar')
            print('2. Depositar')
            print('3. Verificar Saldo')            
        else:
            print('Usuario ou senha incorretos, digite novamente')
            
    elif opcoes == '2':
        print('Obrigado por Usar o ATM PY BANK!')
        break
    else:
        print('Opção INVÁLIDA.')

        

    
        
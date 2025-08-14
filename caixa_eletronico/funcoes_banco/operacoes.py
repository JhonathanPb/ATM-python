import json
import os

def carregar_dados():
    try:
        with open ("dados/contas.json", "r") as arquivos:
            contas = json.load(arquivos)
            return contas
    except FileNotFoundError:
        return {}
    
def salvar_dados(dados_usuario):
    with open("dados/contas.json", "w") as arquivos:
        json.dump(dados_usuario, arquivos)

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def verificar_dados(contas, numero_conta, senha):
    if numero_conta in contas:
        
        if contas[numero_conta]['senha'] == senha:
            return True
    
    return False

def sacar(contas, numero_conta, valor):
    saldo_atual = contas[numero_conta]['saldo']
    
    if valor > 0 and saldo_atual >= valor:
        novo_saldo = saldo_atual - valor
        
        contas[numero_conta]['saldo'] = novo_saldo
        salvar_dados(contas)
        
        return valor
    else:
        return None
        
  
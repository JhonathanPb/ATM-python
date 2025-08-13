import json

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
  
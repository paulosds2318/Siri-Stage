# Pedro Vinicius e Sérgio Gonçalves - CRUD de Empresas

import json
import os

CAMINHO = "data/empresas.json"

def carregar_empresas():
    if not os.path.exists(CAMINHO):
        return []
    with open(CAMINHO, "r") as arquivo:
        return json.load(arquivo)

def salvar_empresas(empresas):
    with open(CAMINHO, "w") as arquivo:
        json.dump(empresas, arquivo, indent=4)

def adicionar_empresa(empresa):
    empresas = carregar_empresas()
    empresas.append(empresa)
    salvar_empresas(empresas)

def listar_empresas():
    return carregar_empresas()
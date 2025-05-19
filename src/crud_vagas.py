# Paulo Marrocos e Cauã dos Santos - CRUD de Vagas

import json
import os

CAMINHO = "data/vagas.json"

def carregar_vagas():
    if not os.path.exists(CAMINHO):
        return []
    with open(CAMINHO, "r") as arquivo:
        return json.load(arquivo)

def salvar_vagas(vagas):
    with open(CAMINHO, "w") as arquivo:
        json.dump(vagas, arquivo, indent=4)

def adicionar_vaga(vaga):
    vagas = carregar_vagas()
    vagas.append(vaga)
    salvar_vagas(vagas)

def listar_vagas():
    return carregar_vagas()
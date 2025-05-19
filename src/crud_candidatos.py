# Luiz Henrique e Pedro Marrocos - CRUD de Candidatos

import json
import os

CAMINHO = "data/candidatos.json"

def carregar_candidatos():
    if not os.path.exists(CAMINHO):
        return []
    with open(CAMINHO, "r") as arquivo:
        return json.load(arquivo)

def salvar_candidatos(candidatos):
    with open(CAMINHO, "w") as arquivo:
        json.dump(candidatos, arquivo, indent=4)

def adicionar_candidato(candidato):
    candidatos = carregar_candidatos()
    candidatos.append(candidato)
    salvar_candidatos(candidatos)

def listar_candidatos():
    return carregar_candidatos()
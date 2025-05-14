# Pedro Marrocos - CRUD de Vagas (empresas criam/editam/excluem/listam vagas)
import json
import os
CAMINHO = "vagas.json"

def adcionar_vagas():
    titulo = str(input("Título da vaga: "))
    empresa = str(input("Empresa: "))
    local = str(input("Local: "))
    vaga = {"titulo": titulo, "empresa": empresa, "local": local}
    vagas = carregar_vagas()
    vagas.append (vaga)
    salvar_vagas (vagas)
    print("✅ Vaga adicionada com sucesso!")
    
def carregar_vagas():
    if not os.path.exists(CAMINHO):
        return []
try:
    with open(CAMINHO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)
except (json.JSONDecodeError, IOError):
    return []

def salvar_vagas():
    


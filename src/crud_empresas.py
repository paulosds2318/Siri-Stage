# Pedro Vinicius - CRUD de Empresas (perfil da Empresa: criar/editar/excluir/ver)

import json
import os

caminho = "data/empresas.json"

# Função de carregar os dados JSON e retornar uma lista das empresas
def carregar_empresas():
    if not os.path.exists(caminho):
        return []
    with open(caminho, "r") as arquivo:
        return json.load(arquivo)

# Função de salvar as empresas em um arquivo JSON    
def salvar_empresas(empresas):
    with open(caminho, "w") as arquivo:
        json.dump(empresas, arquivo, indent=4)

# Função de adicionar uma nova empresa
def criar_empresa(nome, cnpj, endereco):
    empresas = carregar_empresas()
    nova_empresa = {
        "nome": nome,
        "cnpj": cnpj,
        "endereco": endereco
    }
    empresas.append(nova_empresa)
    salvar_empresas(empresas)

# Teste de carregamento
if __name__ == "__main__":
    empresas = carregar_empresas()
    if empresas:
        print("\33[43mDados carregados com sucesso!\33[m")
    else:
        print("\33[44mNenhuma empresa encontrada.\33[m")

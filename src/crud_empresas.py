# Pedro Vinicius e Sérgio Gonçalves - CRUD de Empresas

import json # Importa o módulo JSON para manipulação de arquivos JSON
import os # Importa o módulo OS para interações com o sistema operacional

CAMINHO = "data/empresas.json" 

def atualizar_empresa(indice, empresa_atualizada): # Atualiza uma empresa existente pelo índice
    empresas = carregar_empresas() # Carrega as empresas existentes
    if 0 <= indice < len(empresas): # Verifica se o índice está dentro do intervalo válido
        empresas[indice] = empresa_atualizada # Atualiza a empresa no índice especificado
        salvar_empresas(empresas) # Salva as alterações
        return True
    return False

def remover_empresa(indice): # Remove uma empresa existente pelo índice
    empresas = carregar_empresas() # Carrega as empresas existentes
    if 0 <= indice < len(empresas): # Verifica se o índice está dentro do intervalo válido
        empresas.pop(indice) # Remove a empresa do índice especificado
        salvar_empresas(empresas) # Salva as alterações
        return True
    return False

def obter_empresa_mais_recente(): # Obtém a última empresa cadastrada
    empresas = carregar_empresas() # Carrega as empresas existentes
    if empresas: # Verifica se há empresas cadastradas
        return empresas[-1] # Retorna a última empresa da lista
    return None

def editar_empresa(novos_dados):
    empresas = carregar_empresas() # Carrega as empresas
    if empresas: # Verifica se há empresas cadastradas
        empresas[-1] = novos_dados # Atualiza a última empresa cadastrada
        salvar_empresas(empresas) # Salva as alterações
        return True
    return False
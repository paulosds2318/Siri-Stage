import json
import os
from random import randint

caminho_arquivo = "data/candidatos.json"

def salvar_json(lista_usuarios, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'w', encoding='utf-8') as f:
            json.dump(lista_usuarios, f, indent=4, ensure_ascii=False)
        print(f"Dados salvos com sucesso em {caminho_arquivo}!")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar em JSON: {e}")


def menu_inicial():
    print("1 - Criar Usuário")
    print("2 - Listar Usuário")
    print("3 - Editar Usuário")
    print("4 - Deletar Usuário")
    print("0 - Encerrar o programa")


def carregar_usuario():
    if os.path.exists(caminho_arquivo):
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    else:
        return []


def adicionar_usuario():
    lista_de_usuarios = carregar_usuario()
    novo_usuario = {}
    novo_usuario["Nome"] = str(input("Nome do usuário: "))
    novo_usuario["Idade"] = int(input("Digite sua idade: "))
    novo_usuario["Sexo"] = str(input("Qual seu sexo? "))
    novo_usuario["ID"] = randint(0, 100000)
    lista_de_usuarios.append(novo_usuario.copy())
    salvar_json(lista_de_usuarios, caminho_arquivo)
    print("-" * 50)
    print(f'Usuário Cadastrado Com Sucesso! ID: {novo_usuario["ID"]}')
    print("-" * 50)


def listar_usuario():
    lista_de_usuarios = carregar_usuario()
    if not lista_de_usuarios:
        print("Não há usuários cadastrados!")
    print("Lista de usuários cadastrados:")
    print("-"*50)
    for pessoa in lista_de_usuarios:
        print(f"Nome: {pessoa['Nome']} / Idade: {pessoa['Idade']} / Sexo: {pessoa['Sexo']} / ID: {pessoa['ID']} ")
        print("-"*50)


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
        print("-" * 50)
        print("Não há usuários cadastrados!")
        print("-" * 50)
    else:
        print("-" * 50)
        print("Lista de usuários cadastrados:")
        print("-" * 50)
        for pessoa in lista_de_usuarios:
            print(f"Nome: {pessoa['Nome']} / Idade: {pessoa['Idade']} / Sexo: {pessoa['Sexo']} / ID: {pessoa['ID']} ")
            print("-" * 50)


def editar_usuario():
    lista_de_usuarios = carregar_usuario()
    id_usuario_str = input("Digite o ID do usuário que você quer editar: ")
    usuario_encontrado = None
    indice_usuario = -1

    for i, usuario in enumerate(lista_de_usuarios):
        if str(usuario["ID"]) == id_usuario_str:
            usuario_encontrado = usuario
            indice_usuario = i
            break

    if usuario_encontrado:
        print("-" * 30)
        print("Usuário encontrado:")
        print(f"Nome: {usuario_encontrado['Nome']}")
        print(f"Idade: {usuario_encontrado['Idade']}")
        print(f"Sexo: {usuario_encontrado['Sexo']}")
        print(f"ID: {usuario_encontrado['ID']}")
        print("-" * 30)

        campo_para_editar = input("Qual informação você gostaria de editar? (Nome, Idade, Sexo): ").strip().lower()

        if campo_para_editar == "nome":
            novo_nome = input("Digite o novo nome: ")
            lista_de_usuarios[indice_usuario]["Nome"] = novo_nome
            print("Nome atualizado com sucesso!")
        elif campo_para_editar == "idade":
            nova_idade_str = input("Digite a nova idade: ")
            try:
                nova_idade = int(nova_idade_str)
                lista_de_usuarios[indice_usuario]["Idade"] = nova_idade
                print("Idade atualizada com sucesso!")
            except ValueError:
                print("Idade inválida. A edição não foi realizada.")
        elif campo_para_editar == "sexo":
            novo_sexo = input("Digite o novo sexo: ")
            lista_de_usuarios[indice_usuario]["Sexo"] = novo_sexo
            print("Sexo atualizado com sucesso!")
        else:
            print("Opção de edição inválida.")

        salvar_json(lista_de_usuarios, caminho_arquivo)
    else:
        print("-" * 30)
        print(f"Não foi encontrado nenhum usuário com o ID: {id_usuario_str}")
        print("-" * 30)

def deletar_usuario():
    lista_de_usuarios = carregar_usuario()
    id_para_deletar_str = input("Digite o ID do usuário que você deseja excluir: ")

    indice_para_remover = -1

    for i, usuario in enumerate(lista_de_usuarios):
        if str(usuario["ID"]) == id_para_deletar_str:
            indice_para_remover = i
            break

    if indice_para_remover != -1:
        usuario_excluido = lista_de_usuarios.pop(indice_para_remover)
        salvar_json(lista_de_usuarios, caminho_arquivo)
        print("-" * 30)
        print(f"Usuário com ID {id_para_deletar_str} (Nome: {usuario_excluido['Nome']}) foi excluído com sucesso!")
        print("-" * 30)
    else:
        print("-" * 30)
        print(f"Não foi encontrado nenhum usuário com o ID: {id_para_deletar_str}")
        print("-" * 30)

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("Escolha uma opção:")
        print("1 - Criar Usuário")
        print("2 - Listar Usuários")
        print("3 - Editar Usuário")
        print("4 - Deletar Usuário")
        print("0 - Encerrar o programa")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            adicionar_usuario()
        elif opcao == "2":
            listar_usuario()
        elif opcao == "3":
            editar_usuario()
        elif opcao == "4":
            deletar_usuario()
        elif opcao == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
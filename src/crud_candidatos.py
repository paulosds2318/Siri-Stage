# Luiz Henrique - CRUD de Candidatos (perfil do aluno: criar/editar/excluir/ver)
import json
lista_usuarios = []

def menu_inical():
    print("1 - Criar Usuário")
    print("2 - Listar Usuário")
    print("3 - Editar Usuário")
    print("4 - Deletar Usuário")
    print("0 - Encerrar o programa")

def salvar_usuarios_json(nome_arquivo="data/candidatos.json"):
    try:
        with open(nome_arquivo, 'r+') as arquivo_json:
            try:
                dados_existentes = json.load(arquivo_json)
            except json.JSONDecodeError:
                dados_existentes = []

            dados_existentes.extend(lista_usuarios)

            arquivo_json.seek(0)
            json.dump(dados_existentes, arquivo_json, indent=4)
            arquivo_json.truncate()

        print(f"Dados dos candidatos salvos com sucesso em '{nome_arquivo}'")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o arquivo JSON: {e}")

def adicionar_usuario():
    #cria um usuário{} e adiciona a lista de usuário[]
    usuario = {}
    usuario["Nome"] = str(input("Nome do usuário: "))
    usuario["Idade"] = int(input("Digite sua idade: "))
    usuario["Sexo"] = str(input("Qual seu sexo? "))
    lista_usuarios.append(usuario.copy())
    print("-"*50)
    print(f'Usuário Cadastrado Com Sucesso!')
    print("-"*50)
    salvar_usuarios_json()
x
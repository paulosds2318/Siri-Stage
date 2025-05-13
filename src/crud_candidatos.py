#CRUD do perfil dos candidatos (Luís Henrique).
lista_usuarios = []

def menu_inical():
    print("1 - Criar Usuário")
    print("2 - Listar Usuário")
    print("3 - Editar Usuário")
    print("4 - Deletar Usuário")


def criar_usuario():
    usuario = {}
    usuario["Nome"] = str(input("Nome do usuário: "))
    usuario["Idade"] = int(input("Digite sua idade: "))
    usuario["Sexo"] = str(input("Qual seu sexo? "))
    lista_usuarios.append(usuario.copy())
    print("-"*50)
    print('Usuário Cadastrado Com Sucesso! ')
    print("-"*50)
    print(lista_usuarios)
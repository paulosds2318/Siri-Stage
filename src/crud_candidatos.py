#CRUD do perfil dos candidatos (Luís Henrique).
lista_usuarios = []
def criar_usuario():
    usuario = {}
    usuario["Nome"] = str(input("Nome do usuário: "))
    usuario["Idade"] = int(input("Digite sua idade: "))
    usuario["Sexo"] = str(input("Qual seu sexo? "))
    lista_usuarios.append(usuario.copy())
    print(lista_usuarios)
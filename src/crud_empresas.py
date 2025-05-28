import json
from time import sleep
import os

def carregar_empresas():
    try:
        with open('empresas.json', 'r', encoding='utf-8') as arq:
            dados = json.load(arq)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = []
    return dados

def escrever_empresas(dados):
    try:
        with open('empresas.json', 'w', encoding='utf-8') as arq:
            json.dump(dados, arq, indent=8, ensure_ascii=False)
    except:
        return False
    
def criar_empresas():
    dados_empresas = carregar_empresas()

    nome = input('Digite o nome: ')
    cnpj = input('Digite o cnpj: ')
    endereço = input('Digite o endereço: ')
    gmail = input('Digite o gmail: ')
    contato = input('Digite o contato: ')
    senha = input('Digite o senha: ')

    dados_empresas.append({'nome': nome, 'cnpj': cnpj, 'endereço': endereço, 'gmail': gmail, 'contato': contato, 'senha': senha})

    escrever_empresas(dados_empresas)

    if escrever_empresas(dados_empresas) == False:
        print('Não foi possivel adicionar sua empresa')
    else:
        print('Empresa adicionada com sucesso!')

def editar_empresas(nome):
    dados = carregar_empresas()

    for empresa in dados:
        if empresa['nome'] == nome:
            print(f'Esse é o nome da sua empresa: {empresa['nome']}')
            novo_nome = input('Digite o novo nome: ')
            empresa['nome'] = novo_nome

            print(f'Esse é o cnpj da sua empresa: {empresa['cnpj']}')
            novo_cnpj = input('Digite o novo cnpj: ')
            empresa['cnpj'] = novo_cnpj

            print(f'Esse é o endereço da sua empresa: {empresa['endereço']}')
            novo_endereco = input('Digite o novo endereço: ')
            empresa['endereço'] = novo_endereco

            print(f'Esse é o gmail da sua empresa: {empresa['gmail']}')
            novo_gmail = input('Digite o novo Gmail: ')
            empresa['gmail'] = novo_gmail

            print(f'Esse é o contato da sua empresa: {empresa['contato']}')
            novo_contato = input('Digite o novo contato: ')
            empresa['contato'] = novo_contato

            print(f'Esse é a senha da sua empresa: {empresa['senha']}')
            novo_senha = input('Digite a nova senha: ')
            empresa['senha'] = novo_senha

            escrever_empresas(dados)
            print('Empresa atualizada com sucesso!')
            concluido = True
            break
        concluido = False
    if concluido == False:
        print('Não foi possivel encontrar sua empresa!')

def ver_empresas():
    dados = carregar_empresas()
    concluido = False
    for empresa in dados:
        print(f'\nEssa é a empresa {empresa['nome']}:')
        print(f'\nNome: {empresa['nome']}')
        print(f'Cnpj: {empresa['cnpj']}')
        print(f'Endereço: {empresa['endereço']}')
        print(f'Gmail: {empresa['gmail']}')
        print(f'Contato: {empresa['contato']}')
        print(f'Senha: {empresa['senha']}')
        
        print('\nEssas são as empresas')

        concluido = True
    
    if concluido == False:
        print('Não tem empresas registradas')

def excluir_empresas(nome):
    dados = carregar_empresas()

    for empresa in dados:
        if empresa['nome'] == nome:
            print(f'\nEmpresa {empresa['nome']}:')
            print(f'Nome: {empresa['nome']}, Cnpj: {empresa['cnpj']}, Endereço: {empresa['endereço']}, Gmail: {empresa['gmail']} Contato: {empresa['contato']}, Senha: {empresa['senha']}')
            escolha = input('\nDeseja realmente excluir essa empresa? [s/n]').lower().strip()

            match escolha:
                case 's':
                    dados.remove(empresa)
                    print('Empresa removida com sucesso')
                    escrever_empresas(dados)
                case 'n':
                    print('Empresa não foi removida')
            
            concluido = True
            break
        concluido = False
    if concluido == False:
        print('Não foi possivel encontrar sua empresa!')

def menu():
    sleep(3)
    print('\n------Empresas------')
    print('\n 1. Ver Empresas')
    print(' 2. Criar Empresas')
    print(' 3. Editar Empresas')
    print(' 4. Excluir Empresas')
    print(' 5. Sair do Programa')

def main():
    while True:
        menu()
        escolha = int(input('Escolha uma das opções acima: '))

        match escolha:
            case 1:
                ver_empresas()
            case 2:
                criar_empresas()
            case 3:
                nome = input('Digite o nome da empresa que deseja editar: ')
                editar_empresas(nome)
            case 4:
                nome = input('Digite o nome da empresa que deseja excluir: ')
                excluir_empresas(nome)
            case 5:
                break
            case __:
                print('Opção invalida!')

main()
from flask import Flask, request, render_template, jsonify, redirect
from crud_candidatos import adicionar_candidato, carregar_candidatos, remover_candidato, editar_candidato
from crud_empresas import adicionar_empresa, carregar_empresas, remover_empresa, editar_empresa
from crud_vagas import adicionar_vaga, carregar_vagas, remover_vaga, editar_vaga

app = Flask(__name__)

@app.route('/') # Rota para a página inicial
def home():
    return render_template("index.html")

# Candidatos

@app.route('/candidatos') # Rota para a página de candidatos
def candidatos():
    return render_template("candidatos.html")

@app.route('/cadastro-candidato', methods=['POST']) # Cadastrar Candidato
def cadastro_candidato(): 
    dados = request.json # Coleta os dados do formulário

    candidato = { # Cria um dicionário com os dados do candidato
        "nome": dados.get("nome"),
        "email": dados.get("email"),
        "telefone": dados.get("telefone"),
        "curso": dados.get("curso"),
        "senha": dados.get("senha")
    }

    adicionar_candidato(candidato) # Adiciona o candidato ao arquivo JSON
    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 200

@app.route('/perfil-candidato') # Ler Candidato
def perfil_candidato():
    candidatos = carregar_candidatos() # Carrega todos os candidatos
    candidato = candidatos[-1] if candidatos else None # Pega o último candidato cadastrado
    return render_template("perfil_candidato.html", candidato=candidato)

@app.route('/excluir-candidato', methods=['POST']) # Deletar Candidato
def excluir_candidato():
    candidatos = carregar_candidatos() # Carrega todos os candidatos
    indice_ultimo = len(candidatos) - 1 # Pega o índice do último candidato
    sucesso = remover_candidato(indice_ultimo) # Remove o candidato
    # Verifica se a remoção foi bem-sucedida
    if sucesso:
        return jsonify({"mensagem": "Candidato excluído com sucesso!"}), 200
    else:
        return jsonify({"mensagem": "Erro ao excluir o candidato."}), 400

@app.route('/editar-candidato', methods=['GET', 'POST']) # Rota para editar Candidato
def editar_candidato_view():
    candidatos = carregar_candidatos() # Carrega todos os candidatos
    if not candidatos: # Se não houver candidatos, redireciona para a home
        return redirect('/')
    
    candidato = candidatos[-1] # Pega o último candidato cadastrado
    if request.method == 'POST': # Se o método for POST, significa que o formulário foi enviado
        dados = request.form # Coleta os dados do formulário

        novos_dados = { # Cria um dicionário com os novos dados do candidato
            "nome": dados.get("nome"),
            "email": dados.get("email"),
            "telefone": dados.get("telefone"),
            "curso": dados.get("curso")
        }

        editar_candidato(novos_dados) # Edita o candidato com os novos dados
        return redirect('/perfil-candidato') # Redireciona para o perfil do candidato após a edição
    
    return render_template('editar_candidato.html', candidato=candidato)

# Empresas

@app.route('/empresas') # Rota para a página de empresas
def empresas(): 
    return render_template("empresas.html")

@app.route('/cadastro-empresa', methods=['POST']) # Rota para cadastrar Empresa
def cadastro_empresa():
    dados = request.json # Coleta os dados do formulário

    empresa = { # Cria um dicionário com os dados da empresa
        "nome": dados.get("nome"),
        "cnpj": dados.get("cnpj"),
        "endereco": dados.get("endereco", ""),
        "email": dados.get("email"),
        "telefone": dados.get("telefone"),
        "senha": dados.get("senha")
    }

    adicionar_empresa(empresa) # Adiciona a empresa ao arquivo JSON
    return jsonify({"mensagem": "Empresa cadastrada com sucesso!"}), 200

@app.route('/perfil-empresa') # Rota para ler Empresa
def perfil_empresa():
    empresas = carregar_empresas() # Carrega todas as empresas
    empresa = empresas[-1] if empresas else None # Pega a última empresa cadastrada
    return render_template("perfil_empresa.html", empresa=empresa)

@app.route('/excluir-empresa', methods=['POST']) # Rota para deletar Empresa
def excluir_empresa(): 
    empresas = carregar_empresas() # Carrega todas as empresas
    indice_ultima = len(empresas) - 1 # Pega o índice da última empresa
    sucesso = remover_empresa(indice_ultima) # Remove a empresa
    if sucesso:
        return jsonify({"mensagem": "Empresa excluída com sucesso!"}), 200
    else:
        return jsonify({"mensagem": "Erro ao excluir a empresa."}), 400
    
@app.route('/editar-empresa', methods=['GET', 'POST']) # Rota para editar Empresa
def editar_empresa_view():
    empresas = carregar_empresas() # Carrega todas as empresas
    if not empresas: # Se não houver empresas cadastradas, redireciona para a home
        return redirect('/')

    empresa = empresas[-1]  # A última empresa cadastrada

    if request.method == 'POST': # Se o método for POST, significa que o formulário foi enviado
        dados = request.form # Coleta os dados do formulário

        novos_dados = { # Cria um dicionário com os novos dados da empresa
            "nome": dados.get("nome"),
            "cnpj": dados.get("cnpj"),
            "endereco": dados.get("endereco"),
            "email": dados.get("email"),
            "telefone": dados.get("telefone")
        }

        editar_empresa(novos_dados) # Edita a empresa com os novos dados
        return redirect('/perfil-empresa')

    return render_template('editar_empresa.html', empresa=empresa)

# Vagas

@app.route('/criar-vagas') # Rota para criar Vagas
def vagas():
    return render_template("criar_vagas.html")

@app.route('/criar-vaga', methods=['POST']) # Rota para cadastrar Vaga
def criar_vaga():
    dados = request.json # Coleta os dados do formulário

    empresas = carregar_empresas() # Carrega todas as empresas
    nome_empresa = empresas[-1]["nome"] if empresas else None # Pega o nome da última empresa cadastrada

    vaga = { # Cria um dicionário com os dados da vaga
        "titulo": dados.get("titulo"),
        "descricao": dados.get("descricao"),
        "local": dados.get("local"),
        "salario": dados.get("salario"),
        "empresa": nome_empresa
    }

    adicionar_vaga(vaga) # Adiciona a vaga ao arquivo JSON
    return jsonify({"mensagem": "Vaga criada com sucesso!"}), 200

@app.route('/vagas') # Rota para listar Vagas
def listar_vagas():
    vagas = carregar_vagas() # Carrega todas as vagas
    return render_template("vagas_candidato.html", vagas=vagas)

@app.route('/minhas-vagas') # Rota para listar as vagas da empresa
def minhas_vagas():
    empresas = carregar_empresas() # Carrega todas as empresas
    if not empresas: # Se não houver empresas cadastradas, retorna uma mensagem de erro
        return "Nenhuma empresa cadastrada.", 404

    nome_empresa = empresas[-1]["nome"]  # Pega o nome da última empresa cadastrada

    todas_vagas = carregar_vagas() # Carrega todas as vagas
    minhas_vagas = [vaga for vaga in todas_vagas if vaga.get("empresa") == nome_empresa] # Filtra as vagas que pertencem à empresa pelo nome

    return render_template('vagas_empresa.html', vagas=minhas_vagas, nome_empresa=nome_empresa)

@app.route('/excluir-vaga', methods=['POST']) # Rota para excluir Vaga
def excluir_vaga():
    dados = request.get_json() # Coleta os dados do formulário
    vaga_id = dados.get('id') # Pega o ID da vaga a ser excluída

    if remover_vaga(vaga_id): # Tenta remover a vaga pelo ID
        return jsonify({'mensagem': 'Vaga excluída com sucesso!'}), 200
    else:
        return jsonify({'erro': 'Vaga não encontrada.'}), 404
    
@app.route('/editar-vaga/<vaga_id>', methods=['GET', 'POST']) # Rota para editar Vaga
def editar_vaga_view(vaga_id):
    vagas = carregar_vagas() # Carrega todas as vagas
    vaga = next((vaga for vaga in vagas if vaga.get("id") == vaga_id), None) # Busca a vaga pelo ID fornecido

    if not vaga: # Se a vaga não for encontrada, retorna uma mensagem de erro
        return "Vaga não encontrada.", 404

    if request.method == 'POST': # Se o método for POST, significa que o formulário foi enviado
        dados = request.form # Coleta os dados do formulário

        novos_dados = { # Cria um dicionário com os novos dados da vaga
            "titulo": dados.get("titulo"),
            "descricao": dados.get("descricao"),
            "local": dados.get("local"),
            "salario": dados.get("salario")
        }

        editar_vaga(vaga_id, novos_dados) # Edita a vaga com os novos dados
        return redirect('/minhas-vagas') # Redireciona para a lista de vagas da empresa após a edição

    return render_template('editar_vaga.html', vaga=vaga)

if __name__ == '__main__':
    app.run(debug=True)
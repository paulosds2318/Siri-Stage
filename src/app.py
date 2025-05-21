from flask import Flask, request, render_template, jsonify
from crud_candidatos import adicionar_candidato, carregar_candidatos, remover_candidato
from crud_empresas import adicionar_empresa, carregar_empresas, remover_empresa
from crud_vagas import adicionar_vaga   

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# Candidatos

@app.route('/candidatos')
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

@app.route('/vagas-candidato') # Ler Vagas
def vagas_candidato():
    return render_template("vagas_candidato.html")

@app.route('/perfil-candidato') # Ler Candidato
def perfil_candidato():
    candidatos = carregar_candidatos()
    candidato = candidatos[-1] if candidatos else None
    return render_template("perfil_candidato.html", candidato=candidato)

@app.route('/excluir-candidato', methods=['POST']) # Deletar Candidato
def excluir_candidato():
    candidatos = carregar_candidatos()
    indice_ultimo = len(candidatos) - 1
    sucesso = remover_candidato(indice_ultimo)
    if sucesso:
        return jsonify({"mensagem": "Candidato excluído com sucesso!"}), 200
    else:
        return jsonify({"mensagem": "Erro ao excluir o candidato."}), 400

# Empresas

@app.route('/empresas') 
def empresas(): 
    return render_template("empresas.html")

@app.route('/cadastro-empresa', methods=['POST']) # Cadastrar Empresa
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

@app.route('/perfil-empresa') # Ler Empresa
def perfil_empresa():
    empresas = carregar_empresas() # Carrega todas as empresas
    empresa = empresas[-1] if empresas else None # Pega a última empresa cadastrada
    return render_template("perfil_empresa.html", empresa=empresa) # Renderiza o template com a empresa

@app.route('/excluir-empresa', methods=['POST']) # Deletar Empresa
def excluir_empresa(): 
    empresas = carregar_empresas() # Carrega todas as empresas
    indice_ultima = len(empresas) - 1 # Pega o índice da última empresa
    sucesso = remover_empresa(indice_ultima) # Remove a empresa
    if sucesso:
        return jsonify({"mensagem": "Empresa excluída com sucesso!"}), 200
    else:
        return jsonify({"mensagem": "Erro ao excluir a empresa."}), 400

# Vagas

@app.route('/criar-vagas')
def vagas():
    return render_template("criar_vagas.html")

@app.route('/criar-vaga', methods=['POST'])
def criar_vaga():
    dados = request.json

    vaga = {
        "titulo": dados.get("titulo"),
        "descricao": dados.get("descricao"),
        "local": dados.get("local"),
        "salario": dados.get("salario")
    }

    adicionar_vaga(vaga)
    return jsonify({"mensagem": "Vaga criada com sucesso!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
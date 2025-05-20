from flask import Flask, request, render_template, jsonify
from crud_candidatos import adicionar_candidato
from crud_empresas import adicionar_empresa, carregar_empresas
from crud_vagas import adicionar_vaga

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/candidatos')
def candidatos():
    return render_template("candidatos.html")

@app.route('/cadastro-candidato', methods=['POST'])
def cadastro_candidato():
    dados = request.json

    candidato = {
        "nome": dados.get("nome"),
        "email": dados.get("email"),
        "telefone": dados.get("telefone"),
        "curso": dados.get("curso"),
        "senha": dados.get("senha")
    }

    adicionar_candidato(candidato)
    return jsonify({"mensagem": "Usuário cadastrado com sucesso!"}), 200

@app.route('/empresas')
def empresas():
    return render_template("empresas.html")

@app.route('/cadastro-empresa', methods=['POST'])
def cadastro_empresa():
    dados = request.json

    empresa = {
        "nome": dados.get("nome"),
        "cnpj": dados.get("cnpj"),
        "endereco": dados.get("endereco", ""),
        "email": dados.get("email"),
        "telefone": dados.get("telefone"),
        "senha": dados.get("senha")
    }

    adicionar_empresa(empresa)
    return jsonify({"mensagem": "Empresa cadastrada com sucesso!"}), 200

@app.route('/perfil-empresa')
def perfil_empresa():
    empresas = carregar_empresas()
    empresa = empresas[-1] if empresas else None
    return render_template("perfil_empresa.html", empresa=empresa)

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
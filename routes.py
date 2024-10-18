

from app import app
from flask import render_template
from flask import request
link = "https://flasktintmurilo-default-rtdb.firebaseio.com/"
import requests
import json
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',titulo="Página Inicial")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contatos")

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo="Cadastrar")

@app.route('/atualizacao')
def atualizacao():
    return render_template('atualizacao.html', titulo ="Atualizacão")


@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    try:
        cpf = request.form.get("cpf")
        nome = request.form.get("nome")
        telefone = request.form.get("telefone")
        endereco = request.form.get("endereco")

        dados = {
            "cpf": cpf,
            "nome": nome,
            "telefone": telefone,
            "endereco": endereco
        }
        requisicao = requests.post(f'{link}/cadastro/.json', json=dados)

        if requisicao.status_code == 200:
            return 'Cadastrado com sucesso!', 200
        else:
            return f'Ocorreu um erro ao cadastrar: {requisicao.text}', requisicao.status_code

    except Exception as e:
        return f'Ocorreu um erro: {e}', 500


def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json') #solicito  o dados
        dicionario = requisicao.json()
        return dicionario
    except Exception as e:
        return f'Ocorreu um erro\n + {e}'

@app.route ('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/ cadastro/.json')
        dicionario = requisicao.json()
        idCadastro = "" #coletar o ID
        for codigo in dicionario:
            chave = dicionario[codigo]['cpf']
            if chave == '453535353':
                idCadastro = codigo
            return idCadastro
    except Exception as e:
        return f'Ocorreu um erro\n  {e}'

@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome": "joão"}
        requisicao = requests.patch(f'{link}/cadastro/-O8mrGE9wnwS_zI7GvbI/. json', data=json.dumps(dados))
        return "Atualizado com sucesso!"
    except Exception as e:
        return f'algo deu errado\n {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastro/-O8mrGE9wnwS_zI7GvbI/.json')
        if requisicao.status_code == 200:
            return "Excluído com sucesso!"
        else:
            return f"Erro ao excluir: {requisicao.status_code} - {requisicao.text}"
    except Exception as e:
        return f"Algo deu errado: {e}"



@app.route('/consultarnome')
def consultarNome():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        nomeCadastro = ""

        for chave in dicionario:
            nome = dicionario[chave]['nome']
            if nome == 'mauricio':
                nomeCadastro = nome
                break  #

        if nomeCadastro:
            return nomeCadastro
        else:
            return "Nome não encontrado",

    except Exception as e:
        return f'Algo deu errado\n{e}', 500


@app.route('/consultarendereco')
def consultarendereco():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        enderecoCadastro = ""
        for ende in dicionario:
            endereco = dicionario[ende]['endereco']
            if endereco == 'rwreewrwer':
                enderecoCadastro = ende
                return enderecoCadastro
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/consultarTelefone')
def consultarTelefone():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        telefoneCadastro =""
        for tele in dicionario:
            tele = dicionario[tele]['telefone']
            if tele == '453535353':
                telefoneCadastro = tele
                return telefoneCadastro
    except Exception as e:
        return f'algo deu errado\n {e}'

@app.route('/atualizarTelefone')
def atualizarTelefone():
    try:
        dadosTele = {"telefone":"453535353"}
        requisicao = requests.patch(f'{link}/cadastro/-O8miyEpVGTxlmAj-NX9/.json', data = json.dumps(dadosTele))
        return 'Atualizado com Sucesso!'
    except Exception as e:
        return f'algo deu errado\n{e}'

@app.route('/ConsultarCpf')
def consultarCpf():
    try:
        requisicao = requests.get(f'{link}/cadastro/.json')
        dicionario = requisicao.json()
        consultarCpf = ""
        for cpf in dicionario:
            cpf = dicionario[cpf]['cpf']
            if cpf == 'werreww':
                consultarCpf = cpf
                return consultarCpf
    except Exception as e:
        return f'algo deu errado/n{e}'

@app.route('/atualizarCpf')
def atualizarCpf():
    try:
        dadosCpf = {"telefone":"453535353"}
        requisicao = requests.patch(f'{link}/cadastro/-O8miyEpVGTxlmAj-NX9/.json', data = json.dumps(dadosCpf))
        return 'Atualizado com Sucesso!'
    except Exception as e:
        return f'algo deu errado\n{e}'

@app.route('/consultar')
def consultar():
    return render_template('consultar.html', titulo="Ache suas informações Aqui!")

@app.route('/consultoriaGeral')
def consultoriaGeral():
    try:
        telefone = consultarTelefone()
        nome = consultarNome()
        endereco = consultarendereco()


        return f'Telefone : {telefone}\n, endereco: {endereco}\n, Nome: {nome}'
    except Exception as e:
        return f'Algo deu errado\n {e}'

@app.route('/atualizarNome')
def atualizarNome():
    try:
        dadosNome = {"nome":"mauricio"}
        requisicao = requests.patch(f'{link}/cadastro/-O8miyEpVGTxlmAj-NX9/.json', data = json.dumps(dadosNome))
        return 'Atualizado com Sucesso!'
    except Exception as e:
        return f'algo deu errado\n{e}'

@app.route('/exclusao')
def exclusa():
    return render_template('exclusao.html', titulo="")

@app.route('/cadastrarnovo')
def cadastronovo():
    return render_template('cadastronovo.html', titulo="")


from flask import Flask, request, render_template
import requests

app = Flask(__name__)

from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route('/listarcomcpf', methods=['GET', 'POST'])
def listarcomCpf():
    if request.method == 'GET':
        return render_template('listar.html', titulo="Listar Usuário")

    if request.method == 'POST':
        try:
            cpf = request.form.get("cpf")

            requisicao = requests.get(f'{link}/cadastro/.json')
            dicionario = requisicao.json()

            usuario_encontrado = None
            for codigo in dicionario:
                if dicionario[codigo]['cpf'] == cpf:
                    usuario_encontrado = dicionario[codigo]
                    break

            if not usuario_encontrado:
                return f"CPF {cpf} não encontrado."

            return usuario_encontrado

        except Exception as e:
            return f"Algo deu errado: {str(e)}"



























































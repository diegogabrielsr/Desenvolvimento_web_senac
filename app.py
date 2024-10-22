#importar o Flask, render template e todos os módulos necessários
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# cRiar uma instãncia da aplicação Flask
app = Flask(__name__)

# Fazer uma conexão com o banco de dados SQlite
# Está função será usada para conectar ao banco de dados

def conectar_banco():
    conn = sqlite3.connect('banco.db') # Cria arquivo 'banco.db'
    return conn

def criar_tabela():
    conn = conectar_banco()
    cursor = conn.cursor()
    #criar a tabela 'contatos' com as colunas necessárias
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos(
        id INTERGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        mensagem TEXT NOT NULL,
        tema TEXT NOT NULL)
                   ''')
    conn.commit()
    conn.close()

# Rota para processar o formulário e salvar os dados no banco de dados
@app.route('/contato', methods=['POST'])
def contato():
    # Coletar os dados do formulário
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']
    tema = request.form.get['tema']

    # conectar ao banco de dados e inserir os dados informados
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO contatos (nome, email, mensagem, tema)
    VALUES (?,?,?,?)''', (nome, email, mensagem, tema))
    conn.commit()
    conn.close()

    # redireciona para uma página que mostra os dados salvos
    return redirect(url_for('resultado'))

# Rota para exibir os dados inseridos no banco de dados
@app.route('/resultado')
def resultado():
    # conectar ao banco de dados e buscar os dados
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('SELECT  nome, email, mensagem, tema FROM contatos')
    dados = cursor.fetchall() # pega todos os dados da tabela ' contatos'
    conn.close()

    return render_template('resultado.html', contatos=dados)

if __name__ == '__main__':
    criar_tabela() # chama a função para criar a tabela, se ela não existir
    app.run(debug=True)
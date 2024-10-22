# importação do Flask e dos modulos necessarios do Flask
from flask import Flask, render_template, request

#Criasr uma instãncia da aplicação do Flask, O nome '__nama__'
#define o nome do módulo atual, essa linha informa ao Flask
#onde encontrar os arquivos como templates e estáticos,
app = Flask(__name__)

# definir a rota principal da aplicação. Essa função é chamada 
# quando acessamos a URL raiz '/'
@app.route('/')
def index():
    # O render_template busca um arquivo HTML na pasta 'template'
    # e realiza a renderização no navegador
    return render_template('index.html')

@app.route('/contato', methods=['POST'])
def contato():
    # coleta os dados do formulário enviados via 'POST'
    # Os nomes 'nome', 'email', 'mensagem', 'tema' devem
    # corresponder aos 'name' dos campos HTML
    nome = request.form['nome']
    email = request.form['email']
    mensagem = request.form['mensagem']
    tema = request.form['tema']

    return f'''
    <h1>Obrigado, {nome}</h1>
    <p>Recebemos sua mensagem:</p>
    <p><strong>E-mail:</strong> {email}</p>
    <p><strong>Mensagem:</strong>{mensagem}</p>
    <p><strong>Tema:</strong>{tema}</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)

# /

@app.route('/', methods=['GET'])
def index():
    return "<h1>Turma 1M<h1>"

@app.route('/teste', methods=['POST'])
def teste():
    return "um teste estranho"
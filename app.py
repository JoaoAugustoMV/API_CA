import re
from EPI import  EPI
from flask import Flask, json

app = Flask(__name__)

@app.route('/')
def ola_mundo():
    return 'Ola, flask'

# <ca> = Numero do ca passado como parametro no URL
@app.route('/api/ca/<ca>', methods=['GET'])
def buscarEPI(ca):
    print(ca)
    epi = EPI(ca)
    return json.jsonify(epi.receberEPI())


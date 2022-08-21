import re
from EPI import  EPI
from flask import Flask, json
import flask

app = Flask(__name__)

print(flask.__version__)
@app.route('/')
def ola_mundo():
    epi = EPI(44545)
    return json.jsonify(epi.receberEPI())
    

# <ca> = Numero do ca passado como parametro no URL
@app.route('/api/ca/<ca>', methods=['GET'])
def buscarEPI(ca):
    print(ca)
    epi = EPI(ca)
    return json.jsonify(epi.receberEPI())


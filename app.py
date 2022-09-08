import re
from EPI import  EPI
from api_ca3 import EPI2
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

@app.route('/api/ca2/<ca>')
def buscarEPI2(ca):
    print(ca)
    epi = EPI2(ca)
    return json.jsonify(epi.retornarJSON())

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)
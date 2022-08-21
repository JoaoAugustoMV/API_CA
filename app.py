import re
from EPI import  EPI
from flask import Flask, json
import flask

app = Flask(__name__)
epi = EPI(44545)

print(epi.receberEPI())
@app.route('/')
def ola_mundo():
    return 'Ola, flask'

# <ca> = Numero do ca passado como parametro no URL
@app.route('/api/ca/<ca>', methods=['GET'])
def buscarEPI(ca):
    print(ca)
    epi = EPI(ca)
    return json.jsonify(epi.receberEPI())

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)
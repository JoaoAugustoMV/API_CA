import re
from EPI import  EPI
from api_ca3 import EPI2
from flask import Flask, json
from flask import Flask, render_template
from EPI import EPI

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/api/ca/<ca>')
def retornarInfoEPI(ca):
    epi = EPI(ca)
    return epi.retornarJSON()
    
if __name__ == "__main__":
    app.run(debug=True)

from EPI import  EPI
from flask import Flask, json

app = Flask(__name__)

def lambda_handler(event, context):
    console.log(event)
    console.log(context)
    return {
        'statusCode': 200,
        'body': buscarEPI(44545)
    }

@app.route('/')
def ola_mundo():
    return 'Ola, flask'

# <ca> = Numero do ca passado como parametro no URL
@app.route('/api/ca/<ca>', methods=['GET'])
def buscarEPI(ca):
    print(ca)
    epi = EPI(ca)
    return json.jsonify(epi.receberEPI())

# # JZkkOF5GSU0rUHao1zRPyuoJD+/Agzpo1mDygEeg
# serverless config credentials --provider aws --AKIAZRXRP3SLCPXBPMKY --secret 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

# serverless config credentials --provider aws --key AKIAZRXRP3SLCPXBPMKY --secret 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
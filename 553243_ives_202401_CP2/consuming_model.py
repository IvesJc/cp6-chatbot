from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)


with open('pickle_553243_ives_202401_CP2.pickle', 'rb') as f:
    modelo = pickle.load(f)

@app.route('/prever', methods=['GET'])
def prever():
    parametro1 = float(request.args.get('tamanho_peng'))
    parametro2 = float(request.args.get('profund_peng'))
    parametro3 = float(request.args.get('nadadeira_peng'))
    parametro4 = float(request.args.get('peso_peng'))

    entrada = np.array([[parametro1, parametro2, parametro3, parametro4]])
    resultado = modelo.predict(entrada)

    return jsonify({'previsao': resultado.tolist()})



if __name__ == "__main__":
    app.run()
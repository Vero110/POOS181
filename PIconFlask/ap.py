from flask import Flask, render_template

app = Flask(__name__)

# declaración de la ruta principal
@app.route('/')
def index():
    return render_template('BienvenidaAdmin.html')

@app.route('/InicioSesion.html')
def login(): 
    return render_template('InicioSesion.html')

@app.route('/RegistrarP.html')
def registro(): 
    return render_template('RegistrarP.html')
    
@app.route('/GuardarP.html')
def guardar(): 
    return render_template('GuardarP.html')

@app.route('/EliminarP.html')
def eliminar():
    return render_template('EliminarP.html')

@app.route('/ActualizarP.html')
def actualizar():
    return render_template('ActualizarP.html')

@app.route('/BuscarP.html')
def buscar():
    return render_template('BuscarP.html')

@app.route('/CompraP.html')
def compra(): 
    return render_template('CompraP.html')

@app.route('/BuscarU.html')
def buscarU():
    return render_template('BuscarU.html')

@app.route('/ConsultarU.html')
def consultarU():
    return render_template('ConsultarU.html')

@app.route('/ActualizarU.html')
def actualizarU():
    return render_template('ActualizarU.html')

@app.route('/EliminarU.html')
def eliminarU():
    return render_template('EliminarU.html')

@app.route('/RegistrarU.html')
def registrarU():
    return render_template('RegistrarU.html')


# ejecución del servidor
if __name__ == '__main__': 
    app.run(port=5002, debug=True)
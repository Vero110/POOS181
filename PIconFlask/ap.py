from flask import Flask, render_template

app = Flask(__name__)

# declaración de la ruta principal
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/RegistrarP', methods=['POST'])
def registro(): 
    return render_template('RegistrarP.html')
    
@app.route('/GuardarP', methods=['POST'])
def guardar(): 
    return render_template('GuardarP.html')

@app.route('/EliminarP', methods=['POST'])
def eliminar():
    return render_template('EliminarP.html')

@app.route('/ActualizarP', methods=['POST'])
def actualizar():
    return render_template('ActualizarP.html')

@app.route('/BuscarP', methods=['POST'])
def buscar():
    return render_template('BuscarP.html')

@app.route('CompraP', methods=['POST'])
def compra(): 
    return render_template('CompraP.html')

@app.route('BuscarU', methods=['POST'])
def buscarU():
    return render_template('BuscarU.html')

@app.route('ConsultarU', methods=['POST'])
def consultarU():
    return render_template('ConsultarU.html')

@app.route('ActualizarU', methods=['POST'])
def actualizarU():
    return render_template('ActualizarU.html')

@app.route('EliminarU', methods=['POST'])
def eliminarU():
    return render_template('EliminarU.html')

@app.route('RegistrarU', methods=['POST'])
def registrarU():
    return render_template('RegistrarU.html')


# ejecución del servidor
if __name__ == '__main__': 
    app.run(port=5002, debug=True)
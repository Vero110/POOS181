from flask import Flask, render_template
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'proyectointegrador'
app.secret_key = 'mysecretkey'
MySQL = MySQL(app)

# declaración de la ruta principal
@app.route('/')
def index():
    return render_template('Ingreso.html')

@app.route('/BienvenidaAdmin.html')
def admin():
    return render_template('BienvenidaAdmin.html')

@app.route('/BienvenidaUsuario.html')
def usuario():
    return render_template('BienvenidaUsuario.html')

@app.route('/CRUDU.html')
def crudusuarios():
    return render_template('CRUDU.html')

@app.route('/CRUD.html')
def crudadmin():
    return render_template('CRUD.html')

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

@app.route('/ConsultaP.html')
def consultaprod():
    return render_template('ConsultaP.html')

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
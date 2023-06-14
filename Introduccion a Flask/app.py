#importacion de la paqueteria del framework
from flask import Flask 
from flask_mysqldb import MySQL

#inicializacion de la aplicacion: Señalar que va a trabajar con flask 
app = Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= '11082003'
app.config['MYSQL_DB']= 'dbFlask'
mysql = MySQL(app)


#declaracion de la inicializacion de la ruta http://localhost:5000
@app.route('/') #ruta principal
def index(): 
    return "Hola Mundo FLASK"

@app.route('/guardar') 
def guardar(): 
    return "Se guardo en la BD"

@app.route('/eliminar') 
def eliminar(): 
    return "Se elimino en la BD"

#ejecucion del servidor en el puerto 5000
if __name__ == '__main__': 
    app.run(port=5000, debug=True)
    
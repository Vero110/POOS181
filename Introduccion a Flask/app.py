#importacion de la paqueteria del framework
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

#inicializacion de la aplicacion: Señalar que va a trabajar con flask 
app = Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= '11082003'
app.config['MYSQL_DB']= 'dbFlask'
mysql = MySQL(app)


#declaracion de la inicializacion de la ruta http://127.0.0.1:5000
@app.route('/') #ruta principal
def index(): 
    return render_template('index.html')

#ruta http://127.0.0.1:5000/guardar tipo POST para insert 
@app.route('/guardar', methods={'POST'}) #methods=la informacion sera enviada por formulario y llega por POST 
def guardar(): 
    if request.method == 'POST': 
        titulo= request.form['txtTitulo']
        artista= request.form['txtArtista']
        anio= request.form['txtAnio']
        print(titulo, artista, anio)
    return 'Los datos llegaron ;)'

@app.route('/eliminar') 
def eliminar(): 
    return "Se elimino en la BD"

#ejecucion del servidor en el puerto 5000
if __name__ == '__main__': 
    app.run(port=5000, debug=True)
    
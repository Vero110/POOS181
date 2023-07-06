#importacion de la paqueteria del framework
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


#inicializacion de la aplicacion: Señalar que va a trabajar con flask 
app = Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'dbFlask'
app.secret_key = 'mysecretkey'
MySQL = MySQL(app)


#declaracion de la inicializacion de la ruta http://127.0.0.1:5000
@app.route('/') #ruta principal
def index(): 
    CC = MySQL.connection.cursor()
    CC.execute('select * from TB_Albums')
    conAlbums=CC.fetchall()
    #print(conAlbums)
    
    return render_template('index.html', listalbums=conAlbums)

 
#ruta http://127.0.0.1:5000/guardar tipo POST para insert 
@app.route('/guardar', methods=['POST']) #methods=la informacion sera enviada por formulario y llega por POST 
def guardar(): 
    if request.method == 'POST': 
        
        #Aquí pasamos a vaviables el contenido de los input
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
        
        #Conectarnos a la base de datos y ejecutar el insert
        CS = MySQL.connection.cursor()
        CS.execute('insert into TB_Albums(titulo, artista, anio) VALUES(%s,%s,%s)',(Vtitulo, Vartista, Vanio))
        MySQL.connection.commit()
        
    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))
    
@app.route('/editar/<id>') 
def editar(id): 
    cursorID = MySQL.connection.cursor()
    cursorID.execute('select * from TB_Albums where id = %s',(id,))
    consultaID= cursorID.fetchone()
    
    return render_template('editarAlbum.html', album=consultaID)

@app.route('/actualizar/<id>', methods=['POST']) 
def actualizar(id): 
    if request.method == 'POST': 
        varTitulo = request.form['txtTitulo']
        varArtista = request.form['txtArtista']
        varAnio = request.form['txtAnio']
        
        curAct = MySQL.connection.cursor()
        curAct.execute('update TB_Albums set titulo = %s, artista= %s, anio = %s where id = %s', (varTitulo, varArtista, varAnio, id))
        MySQL.connection.commit()
        
    flash('Se actualizaron los datos del Album' + varTitulo)
    return redirect(url_for('index'))


@app.route('/eliminar/<id>')
def eliminar(id):
    cursorDel = MySQL.connection.cursor()
    cursorDel.execute('delete from TB_Albums where id = %s', (id))
    MySQL.connection.commit()
    
    flash('El álbum fue eliminado correctamente')
    return redirect(url_for('index'))


#ejecucion del servidor en el puerto 5000
if __name__ == '__main__': 
    app.run(port=3000, debug=True)
    
from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_mysqldb import MySQL

app = Flask(__name__) 
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='proyectointegrador'
app.secret_key='mysecretkey'
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuarios')
def usuarios():
    return render_template('ingresar.html')

@app.route('/productos')
def productos():
    return render_template('guardarProducto.html')


@app.route('/ingresar', methods=['POST'])
def ingresar():
    if request.method=='POST':
        Vfruta=request.form['txtNombre']
        Vtemporada=request.form['txtCorreo']
        Vprecio=request.form['txtDireccion']
        Vstock=request.form['txtTelefono']

        CS = mysql.connection.cursor()
        CS.execute('insert into guardarusuario(nombre, correo, direccion, telefono) values (%s,%s,%s,%s)', (Vfruta, Vtemporada, Vprecio, Vstock))
        mysql.connection.commit()
    flash('El usuario se ha guardado correctamente')
    return redirect(url_for('index'))

@app.route('/editar')
def editar():
    cursorEdi = mysql.connection.cursor() 
    cursorEdi.execute('select * from guardarusuario')
    conFru = cursorEdi.fetchall( ) 
    return render_template('consulta.html', listaF = conFru) 

@app.route('/actualizarVista/<string:id>')
def actualizarVista(id):
    cursorUpdV = mysql.connection.cursor()
    cursorUpdV.execute('select * from guardarusuario where id = %s', (id,))
    confru = cursorUpdV.fetchone()
    return render_template('editarUsuario.html', UpdateFruta = confru)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varFruta = request.form['txtNombre']
        varTemporada = request.form['txtCorreo']
        varPrecio = request.form['txtDireccion']
        varStock = request.form['txtTelefono']
        cursorUpd = mysql.connection.cursor()
        cursorUpd.execute('update guardarusuario set nombre = %s, correo = %s, direccion = %s, telefono = %s where id = %s', (varFruta, varTemporada, varPrecio, varStock, id))
        mysql.connection.commit()
    flash ('El usuario '+varFruta+' se actualizo correctamente.')
    return redirect(url_for('editar'))

@app.route('/confirmacion/<id>')
def eliminar(id):
    cursorConfi = mysql.connection.cursor()
    cursorConfi.execute('select * from guardarusuario where id = %s', (id,))
    consuF = cursorConfi.fetchone()
    return render_template('eliminarUsuario.html', fruta=consuF)

@app.route("/eliminar/<id>", methods=['POST'])
def eliminarBD(id):
    cursorDlt = mysql.connection.cursor()
    cursorDlt.execute('delete from guardarusuario where id = %s', (id,))
    mysql.connection.commit()
    flash('Se elimino el usuario con id '+ id)
    return redirect(url_for('index'))

#Ejecucion del servidor
if __name__=='__main__':
    app.run(port=5001,debug=True) 

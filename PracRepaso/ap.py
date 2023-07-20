from flask import Flask, render_template, request, redirect, url_for, flash 
from flask_mysqldb import MySQL

app = Flask(__name__) 
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='proyectointegrador'
app.secret_key='mysecretkey'
mysql=MySQL(app)
#ruta principal
@app.route('/')
def index():
    return render_template('index.html')
#rutas de usuario
@app.route('/usuarios')
def usuarios():
    return render_template('ingresar.html')
#rutas de productos
@app.route('/productos')
def productos():
    return render_template('ingresarp.html')
#ruta de compra
@app.route('/compras')
def compras():
    return render_template('ingresarc.html')

# COMPRAS 
@app.route('/comprap', methods=['GET', 'POST'])
def comprap():
    if request.method == 'POST':
        v_nombre = request.form['Nombre']
        v_cantidad = request.form['Cantidad']
        
        if v_nombre and v_cantidad:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO compras (nombre, cantidad) VALUES (%s, %s)', (v_nombre, v_cantidad))
            mysql.connection.commit()
            flash('La compra se ha agregado ')
            return redirect(url_for('index'))
        else:
            flash('Por favor, completa todos los campos')

    return render_template('GuardarUsuario.html')
    
#ADMINISTRAR USUARIOS 
#GUARDAR USUARIOS
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

#FUNCION PARA LA ACTUALIZACION DE LOS DATOS
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

#FUNCION PARA ELIMINAR Y CONFIRMAR
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

#ADMINISTRAR PRODUCTOS 
#guardar productos
@app.route('/ingresarp', methods=['POST'])
def ingresarp():
    if request.method=='POST':
        Vfruta=request.form['txtNombre']
        Vtemporada=request.form['txtDescripcion']
        Vprecio=request.form['txtPrecio']
        Vstock=request.form['txtMarca']

        CS = mysql.connection.cursor()
        CS.execute('insert into guardarproducto(nombre, descripcion, precio, marca) values (%s,%s,%s,%s)', (Vfruta, Vtemporada, Vprecio, Vstock))
        mysql.connection.commit()
    flash('El producto se ha guardado correctamente')
    return redirect(url_for('index'))

#FUNCION PARA LA ACTUALIZACION DE LOS DATOS
@app.route('/editarp')
def editarp():
    cursorEdi = mysql.connection.cursor() 
    cursorEdi.execute('select * from guardarproducto')
    conFru = cursorEdi.fetchall( ) 
    return render_template('consultap.html', listaF = conFru) 

@app.route('/actualizarVistap/<string:id>')
def actualizarVistap(id):
    cursorUpdV = mysql.connection.cursor()
    cursorUpdV.execute('select * from guardarproducto where id = %s', (id,))
    confru = cursorUpdV.fetchone()
    return render_template('editarProducto.html', UpdateFruta = confru)

@app.route('/actualizarp/<id>', methods=['POST'])
def actualizarp(id):
    if request.method == 'POST':
        varFruta = request.form['txtNombre']
        varTemporada = request.form['txtDescripcion']
        varPrecio = request.form['txtPrecio']
        varStock = request.form['txtMarca']
        cursorUpd = mysql.connection.cursor()
        cursorUpd.execute('update guardarproducto set nombre = %s, descripcion = %s, precio = %s, marca = %s where id = %s', (varFruta, varTemporada, varPrecio, varStock, id))
        mysql.connection.commit()
    flash ('El producto '+varFruta+' se actualizo correctamente.')
    return redirect(url_for('editarp'))

#FUNCION PARA ELIMINAR Y CONFIRMAR
@app.route('/confirmacionp/<id>')
def eliminarp(id):
    cursorConfi = mysql.connection.cursor()
    cursorConfi.execute('select * from guardarproducto where id = %s', (id,))
    consuF = cursorConfi.fetchone()
    return render_template('eliminarProducto.html', fruta=consuF)

@app.route("/eliminarp/<id>", methods=['POST'])
def eliminarBDp(id):
    cursorDlt = mysql.connection.cursor()
    cursorDlt.execute('delete from guardarproducto where id = %s', (id,))
    mysql.connection.commit()
    flash('Se elimino el producto con id '+ id)
    return redirect(url_for('index'))

#Ejecucion del servidor
if __name__=='__main__':
    app.run(port=5001,debug=True) 

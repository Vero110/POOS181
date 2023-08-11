from flask import Flask, render_template, request, redirect, url_for, flash
import pyodbc

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

server = 'localhost'
database = 'proyectointegrador'
username = '' 
password = ''  
connection_string = f'DRIVER=SQL Server;SERVER={server};DATABASE={database};UID={username};PWD={password}'

def get_db_connection():
    return pyodbc.connect(connection_string)

def execute_query(query, params=None):
    connection = get_db_connection()
    cursor = connection.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    connection.commit()
    cursor.close()
    connection.close()
    return result

@app.route('/')
def bienvenida():
    return render_template('bienvenida.html')

@app.route('/indexp')
def indexp():
    return render_template('indexp.html')

@app.route('/usuarios')
def usuarios():
    return render_template('ingresar.html')

@app.route('/productos')
def productos():
    return render_template('ingresarp.html')

@app.route('/compra')
def compra():
    return render_template('ingresarcompras.html')

@app.route('/carrito')
def carrito():
    query = 'SELECT * FROM comprasporusuarios'
    result = execute_query(query)
    return render_template('carrito.html', listaF=result)

@app.route('/compras')
def compras():
    query = 'SELECT * FROM guardarproducto'
    result = execute_query(query)
    return render_template('ingresarc.html', listaF=result)

# Ruta de compra
@app.route('/comprap', methods=['POST'])
def comprap():
    if request.method == 'POST':
        v_nombre = request.form['txtNombre']
        v_descripcion = request.form['txtDescripcion']
        v_precio = request.form['txtPrecio']
        v_marca = request.form['txtMarca']

        query = 'INSERT INTO comprasporusuarios (nombre, descripcion, precio, marca) VALUES (?, ?, ?, ?)'
        params = (v_nombre, v_descripcion, v_precio, v_marca)

        execute_query(query, params)

        flash('La compra se ha agregado')
    return redirect(url_for('compra'))

@app.route('/ingresar', methods=['POST'])
def ingresar():
    if request.method=='POST':
        Vfruta = request.form['txtNombre']
        Vtemporada = request.form['txtCorreo']
        Vprecio = request.form['txtDireccion']
        Vstock = request.form['txtTelefono']

        query = 'INSERT INTO guardarusuario(nombre, correo, direccion, telefono) VALUES (?, ?, ?, ?)'
        params = (Vfruta, Vtemporada, Vprecio, Vstock)

        execute_query(query, params)

        flash('El usuario se ha guardado correctamente')
    return redirect(url_for('usuarios'))

@app.route('/editar')
def editar():
    query = 'SELECT * FROM guardarusuario'
    result = execute_query(query)
    return render_template('consulta.html', listaF=result)

@app.route('/actualizarVista/<string:id>')
def actualizarVista(id):
    query = 'SELECT * FROM guardarusuario WHERE id = ?'
    params = (id,)
    confru = execute_query(query, params)
    return render_template('editarUsuario.html', UpdateFruta=confru)

@app.route('/actualizar/<id>', methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        varFruta = request.form['txtNombre']
        varTemporada = request.form['txtCorreo']
        varPrecio = request.form['txtDireccion']
        varStock = request.form['txtTelefono']
        query = 'UPDATE guardarusuario SET nombre = ?, correo = ?, direccion = ?, telefono = ? WHERE id = ?'
        params = (varFruta, varTemporada, varPrecio, varStock, id)
        execute_query(query, params)
        flash('El usuario ' + varFruta + ' se actualizó correctamente.', 'success')
    return redirect(url_for('usuarios'))

@app.route('/confirmacion/<id>')
def eliminar(id):
    query = 'SELECT * FROM guardarusuario WHERE id = ?'
    params = (id,)
    consuF = execute_query(query, params)
    return render_template('eliminarUsuario.html', fruta=consuF)

@app.route("/eliminar/<id>", methods=['POST'])
def eliminarBD(id):
    query = 'DELETE FROM guardarusuario WHERE id = ?'
    params = (id,)
    execute_query(query, params)
    flash('Se eliminó el usuario con id ' + id)
    return redirect(url_for('usuarios'))

@app.route('/ingresarp', methods=['POST'])
def ingresarp():
    if request.method=='POST':
        Vfruta = request.form['txtNombre']
        Vtemporada = request.form['txtDescripcion']
        Vprecio = request.form['txtPrecio']
        Vstock = request.form['txtMarca']

        query = 'INSERT INTO guardarproducto(nombre, descripcion, precio, marca) VALUES (?, ?, ?, ?)'
        params = (Vfruta, Vtemporada, Vprecio, Vstock)

        execute_query(query, params)

        flash('El producto se ha guardado correctamente')
    return redirect(url_for('productos'))

@app.route('/editarp')
def editarp():
    query = 'SELECT * FROM guardarproducto'
    result = execute_query(query)
    return render_template('consultap.html', listaF=result)

@app.route('/actualizarVistap/<string:id>')
def actualizarVistap(id):
    query = 'SELECT * FROM guardarproducto WHERE id = ?'
    params = (id,)
    confru = execute_query(query, params)
    return render_template('editarProducto.html', UpdateFruta=confru)

@app.route('/actualizarp/<id>', methods=['POST'])
def actualizarp(id):
    if request.method == 'POST':
        varFruta = request.form['txtNombre']
        varTemporada = request.form['txtDescripcion']
        varPrecio = request.form['txtPrecio']
        varStock = request.form['txtMarca']
        query = 'UPDATE guardarproducto SET nombre = ?, descripcion = ?, precio = ?, marca = ? WHERE id = ?'
        params = (varFruta, varTemporada, varPrecio, varStock, id)
        execute_query(query, params)
        flash('El producto ' + varFruta + ' se actualizó correctamente.')
    return redirect(url_for('productos'))

@app.route('/confirmacionp/<id>')
def eliminarp(id):
    query = 'SELECT * FROM guardarproducto WHERE id = ?'
    params = (id,)
    consuF = execute_query(query, params)
    return render_template('eliminarProducto.html', fruta=consuF)

@app.route("/eliminarp/<id>", methods=['POST'])
def eliminarBDp(id):
    query = 'DELETE FROM guardarproducto WHERE id = ?'
    params = (id,)
    execute_query(query, params)
    flash('Se eliminó el producto con id ' + id)
    return redirect(url_for('productos'))

@app.route('/consulta')
def consulta():
    return render_template('consultar.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    varfrutas = request.form.get('txtNombre', False)
    query = 'SELECT * FROM guardarusuario WHERE nombre = ?'
    params = (varfrutas,)
    datos = execute_query(query, params)
    return render_template('consultar.html', listaF=datos)

@app.route('/consultap')
def consultap():
    return render_template('consultarp.html')

@app.route('/buscarp', methods=['POST'])
def buscarp():
    varfrutas = request.form.get('txtNombre', False)
    query = 'SELECT * FROM guardarproducto WHERE nombre = ?'
    params = (varfrutas,)
    datos = execute_query(query, params)
    return render_template('consultarp.html', listaF=datos)


# Ejecución del servidor
if __name__ == '__main__':
    app.run(port=5005, debug=True)

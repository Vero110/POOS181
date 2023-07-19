from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyectointegrador'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/usuarios')
def usuarios():
    return render_template('guardarUsuario.html')

@app.route('/productos')
def productos():
    return render_template('guardarProducto.html')

@app.route('/eliminarpro')
def eliminarpro():
    return render_template('eliminarProducto.html')

@app.route('/eliminarusu')
def eliminarusu():
    return render_template('eliminarUsuario.html')

@app.route('/compras')
def compras():
    return render_template('compras.html')

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
    
@app.route('/guardaru', methods=['GET', 'POST'])
def guardaru():
    if request.method == 'POST':
        v_nombre = request.form['Nombre']
        v_correo = request.form['Correo']
        v_direccion = request.form['Direccion']
        v_telefono = request.form['Telefono']

        if v_nombre and v_correo and v_direccion and v_telefono:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO guardarusuario (nombre, correo, direccion, telefono) VALUES (%s, %s, %s, %s)', (v_nombre, v_correo, v_direccion, v_telefono))
            mysql.connection.commit()
            flash('El usuario fue guardado correctamente')
            return redirect(url_for('index'))
        else:
            flash('Por favor, completa todos los campos')

    return render_template('GuardarUsuario.html')

@app.route('/guardarp', methods=['GET', 'POST'])
def guardarp():
    if request.method == 'POST':
        v_nombre = request.form['Nombre']
        v_descripcion = request.form['Descripcion']
        v_precio = request.form['Precio']
        v_marca = request.form['Marca']

        if v_nombre and v_descripcion and v_precio and v_marca:
            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO guardarproducto (nombre, descripcion, precio, marca) VALUES (%s, %s, %s, %s)', (v_nombre, v_descripcion, v_precio, v_marca))
            mysql.connection.commit()

            flash('El producto fue guardado correctamente')
            return redirect(url_for('index'))
        else:
            flash('Por favor, completa todos los campos')

    return render_template('GuardarProducto.html')
  
@app.route('/eliminaru/', methods=['GET', 'POST'])
def eliminaru():
    Vide = request.form['txtUID']
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM guardarusuario WHERE id=%s', Vide)
    mysql.connection.commit()

    flash('Usuario eliminado correctamente')
    return redirect(url_for('index'))

@app.route('/borraru/<id>')
def borraru(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM guardarusuario WHERE id_usuario=%s', (id,))
    consultaID = cursor.fetchone()
    return render_template('eliminarUsuario.html', eliu=consultaID)

@app.route('/eliminarp/', methods=['GET', 'POST'])
def eliminarp():
    Vid = request.form['txtID']
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM guardarproducto WHERE id=%s', Vid)
    mysql.connection.commit()

    flash('Producto eliminado correctamente')
    return redirect(url_for('index'))

@app.route('/borrarp/<id>')
def borrarp(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM guardarproducto WHERE id_producto=%s', (id,))
    consultaID = cursor.fetchone()
    return render_template('eliminarProducto.html', elip=consultaID)

@app.route('/actualizaru/<id>', methods=['GET', 'POST'])
def actualizaru(id):
    if request.method == 'POST':
        v_id = request.form['ID']
        v_nombre = request.form['Nombre']
        v_correo = request.form['Correo']
        v_direccion = request.form['Direccion']
        v_telefono = request.form['Telefono']

        if v_nombre and v_correo and v_direccion and v_telefono:
            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE guardarusuario SET nombre=%s, correo=%s, direccion=%s, telefono=%s WHERE id_usuario=%s', (v_nombre, v_correo, v_direccion, v_telefono, v_id))
            mysql.connection.commit()
            flash('El usuario fue actualizado correctamente')
            return redirect(url_for('index'))
        else:
            flash('Por favor, completa todos los campos')

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM guardarusuario WHERE id_usuario=%s', (id,))
    usuario = cursor.fetchone()

    return render_template('actualizarUsuario.html', actu=usuario)

@app.route('/actualizarp/<id>', methods=['GET', 'POST'])
def actualizarp(id):
    if request.method == 'POST':
        v_id = request.form['ID']
        v_nombre = request.form['Nombre']
        v_descripcion = request.form['Descripcion']
        v_precio = request.form['Precio']
        v_marca = request.form['Marca']

        if v_nombre and v_descripcion and v_precio and v_marca:
            cursor = mysql.connection.cursor()
            cursor.execute('UPDATE guardarproducto SET nombre=%s, descripcion=%s, precio=%s, marca=%s WHERE id_producto=%s', (v_nombre, v_descripcion, v_precio, v_marca, v_id))
            mysql.connection.commit()

            flash('El producto fue actualizado correctamente')
            return redirect(url_for('index'))
        else:
            flash('Por favor, completa todos los campos')

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM guardarproducto WHERE id_producto=%s', (id,))
    producto = cursor.fetchone()

    return render_template('actualizarProducto.html', actp=producto)

@app.route('/editaru/<id>')
def editaru(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM guardarusuario WHERE id_usuario=%s', (id,))
    consultaID = cursor.fetchone()

    return render_template('editarUsuario.html', actu=consultaID)

@app.route('/editarp/<id>')
def editarp(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM guardarproducto WHERE id_producto=%s', (id,))
    consultaID = cursor.fetchone()

    return render_template('actualizarProducto.html', actp=consultaID)

if __name__ == '__main__':
    app.run(port=5003, debug=True)


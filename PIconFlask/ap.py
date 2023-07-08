from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'proyectointegrador'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

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

@app.route('/guardar', methods=['POST'])
def guardarP():
    if request.method == 'POST':
        v_nombre = request.form['Nombre']
        v_descripcion = request.form['Descripcion']
        v_precio = request.form['Precio']
        v_marca = request.form['Marca']
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO guardarproducto (nombre, descripcion, precio, marca) VALUES (%s, %s, %s, %s)', (v_nombre, v_descripcion, v_precio, v_marca))
        mysql.connection.commit()
        
        flash('El producto fue guardado correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar_producto', methods=['POST'])
def eliminar_producto():
    if request.method == 'POST':
        v_id = request.form['ID']

        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM guardarproducto WHERE id=%s', (v_id,))
        mysql.connection.commit()
        
    flash('El producto fue eliminado correctamente')
    return render_template('EliminarP.html')

@app.route('/actualizar_producto', methods=['POST'])
def actualizar_producto():
    if request.method == 'POST':
        v_id = request.form['ID']
        v_nombre = request.form['Nombre']
        v_descripcion = request.form['Descripcion']
        v_precio = request.form['Precio']
        v_marca = request.form['Marca']
        
        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE guardarproducto SET nombre=%s, descripcion=%s, precio=%s, marca=%s WHERE id=%s', (v_nombre, v_descripcion, v_precio, v_marca, v_id))
        mysql.connection.commit()
        
        flash('El producto fue actualizado correctamente')
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

@app.route('/guardar_usuario', methods=['POST'])
def guardar_usuario():
    if request.method == 'POST':
        v_nombre = request.form['Nombre']
        v_correo = request.form['Correo']
        v_direccion = request.form['Direccion']
        v_telefono = request.form['Telefono']
        
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO guardarusuario (nombre, correo, direccion, telefono) VALUES (%s, %s, %s, %s)', (v_nombre, v_correo, v_direccion, v_telefono))
        mysql.connection.commit()
        
        flash('El usuario fue guardado correctamente')
    return render_template('RegistrarU.html')

@app.route('/BuscarU.html')
def buscarU():
    return render_template('BuscarU.html')

@app.route('/ConsultarU.html')
def consultarU():
    return render_template('ConsultarU.html')

@app.route('/actualizar_usuario', methods=['POST'])
def actualizar_usuario():
    if request.method == 'POST':
        v_id = request.form['ID']
        v_nombre = request.form['Nombre']
        v_correo = request.form['Correo']
        v_direccion = request.form['Direccion']
        v_telefono = request.form['Telefono']

        cursor = mysql.connection.cursor()
        cursor.execute('UPDATE guardarusuario SET nombre=%s, correo=%s, direccion=%s, telefono=%s WHERE id=%s', (v_nombre, v_correo, v_direccion, v_telefono, v_id))
        mysql.connection.commit()

        flash('El usuario fue actualizado correctamente')
    return render_template('ActualizarU.html')

@app.route('/eliminar_usuario', methods=['POST'])
def eliminar_usuario():
    if request.method == 'POST':
        v_id = request.form['ID']
        
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM guardarusuario WHERE id=%s', (v_id,))
        mysql.connection.commit()

        
        flash('El usuario fue eliminado correctamente')
    return render_template('EliminarU.html')


# ejecución del servidor
if __name__ == '__main__': 
    app.run(port=5002, debug=True)
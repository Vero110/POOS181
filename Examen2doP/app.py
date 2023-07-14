from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'dbfloreria'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

@app.route('/') 
def index(): 
    CC = mysql.connection.cursor()
    CC.execute('select * from tbfloreria')
    conflor=CC.fetchall()
    #print(conflor)
    return render_template('index.html', listalbums=conflor)

@app.route('/guardar', methods={'POST'}) 
def guardar(): 
    if request.method == 'POST':         
        vnombre= request.form['txtNombre']
        vcantidad= request.form['txtCantidad']
        vprecio= request.form['txtPrecio']
        
        CS = mysql.connection.cursor()
        CS.execute('insert into tbfloreria(nombre, cantidad, precio) VALUES(%s,%s,%s)',(vnombre, vcantidad, vprecio))
        mysql.connection.commit()
        
    flash('La flor se ha registrado')
    return redirect(url_for('index'))

@app.route('/eliminarpro')
def eliminarpro():
    return render_template('eliminarF.html')

@app.route('/eliminarp/', methods=['GET', 'POST'])
def eliminarp():
    Vid = request.form['txtID']
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM tbfloreria WHERE id=%s', Vid)
    mysql.connection.commit()

    flash('flor eliminada correctamente')
    return redirect(url_for('index'))

@app.route('/borrarp/<id>')
def borrarp(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM tbloreria WHERE id_producto=%s', (id,))
    consultaID = cursor.fetchone()
    return render_template('eliminarF.html', elip=consultaID)

if __name__ == '__main__': 
    app.run(port=5005, debug=True)
    
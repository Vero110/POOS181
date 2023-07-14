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
    return render_template('index.html')

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
    
if __name__ == '__main__': 
    app.run(port=5005, debug=True)
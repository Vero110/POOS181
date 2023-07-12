from flask import Flask, render_template, request, redirect,url_for,flash 
from flask_mysqldb import MySQL

app=Flask(__name__) 

app.config['MYSQL_HOST']="localhost" 
app.config['MYSQL_USER']="root" 
app.config['MYSQL_PASSWORD']="" 
app.config['MYSQL_DB']="db_fruteria" 
app.secret_key='mysecretkey' 
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method=='POST':
        VFruta=request.form['txtFruta']
        VTemporada=request.form['txtTemporada']
        Vprecio=request.form['txtPrecio']
        Vstock=request.form['txtStock']

        CS=mysql.connection.cursor()
        CS.execute('insert into tbfrutas(fruta,temporada,precio,stock) values(%s,%s,%s,%s)',(VFruta,VTemporada,Vprecio,Vstock)) 
        mysql.connection.commit()

        flash('Registro agregado correctamente')
    return redirect(url_for('index')) 

@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method=='POST': 
        VFruta=request.form['txtFruta']
        VTemporada=request.form['txtTemporada']
        Vprecio=request.form['txtPrecio']
        Vstock=request.form['txtStock']
    
        curUpdate=mysql.connection.cursor()
        curUpdate.execute('update tbfrutas set fruta=%s, temporada=%s, precio=%s, stock=%s where id=%s', (VFruta,VTemporada,Vprecio,Vstock,id))
        mysql.connection.commit()

    flash('Registro actualizado correctamente')
    return redirect(url_for('index')) 

@app.route('/editar/<id>')
def editar(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from tbfrutas where id= %s', (id,))
    consultaID=curEditar.fetchone()

    return render_template('editarFruteria.html', fruteria=consultaID)

@app.route('/eliminar/<id>',methods=['POST'])
def eliminar(id):
    curDelete=mysql.connection.cursor()
    curDelete.execute('delete from tbfrutas where id=%s', (id)) 
    mysql.connection.commit()

    flash('Registro eliminado correctamente')
    return redirect(url_for('index')) 

@app.route('/borrar-fruta/<id>')
def borrar_fruta(id):
    curBorrar=mysql.connection.cursor()
    curBorrar.execute('select * from tbfrutas where id= %s', (id,))
    consultaID=curBorrar.fetchone()

    return render_template('eliminarFruteria.html', fruteria=consultaID)

@app.route('/consultar')
def borrar():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from tbfrutas')
    consulta=curSelect.fetchall() 
    #print(consulta)
    return render_template('consultarFruteria.html', listaFruteria=consulta)  

@app.route('/buscar/<id>')
def buscar(id):
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from tbfrutas where id=%s', (id,))
    consulta=curSelect.fetchone() 
    #print(consulta)
    return render_template('buscarFruteria.html', listaFruteria=consulta) 

#Ejecucion del servidor
if __name__=='__main__':
    app.run(port=5001,debug=True) 

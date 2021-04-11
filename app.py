from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from config import *

app= Flask(__name__)
app.secret_key="CLAVEDEMARIA" 


conn= sqlite3.connect("data/basedecontactos.db")
c= conn.cursor()




@app.route('/')
def index():
    conn= sqlite3.connect('data/basedecontactos.db')
    c=conn.cursor()

    c.execute('SELECT * FROM flask_contactos ')
    data= c.fetchall()
    print(data)
    conn.commit()
    conn.close()

    return render_template('index.html' , contactos=data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    
    if request.method == 'POST' :
        fullname= request.form['fullname']
        phone= request.form['phone']
        email= request.form['email']

        conn= sqlite3.connect("data/basedecontactos.db")
        c= conn.cursor()

        c.execute('INSERT INTO flask_contactos (fullname, phone, email) VALUES (?, ? , ?) ', (
            fullname, phone, email))

        conn.commit()
        conn.close()

        flash('contacto agregado satisfactoriamente')
        return redirect(url_for('index'))

@app.route('/editar/<id>')
def editar_contacto(id):
    conn=sqlite3.connect('data/basedecontactos.db')
    c=conn.cursor()

    c.execute('SELECT * FROM flask_contactos WHERE id= {0}'.format(id))
    data=c.fetchall()
    return render_template('edit-contacto.html', contacto=data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contactos(id):
    if request.method == 'POST':
        fullname= request.form['fullname']
        phone= request.form['phone']
        email= request.form['email']

        conn= sqlite3.connect('data/basedecontactos.db')
        c=conn.cursor()

        c.execute("""UPDATE flask_contactos
        SET  fullname= '%s' ,
            phone= '%s' ,
            email= '%s'
        WHERE id= '%s'
        """ % (fullname, phone, email, id))

        conn.commit()
        conn.close()

        flash('contacto actualizado sactifactoriamente')
        return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def delete_contacto(id):
    conn=sqlite3.connect('data/basedecontactos.db')
    c=conn.cursor()
    
    c.execute('DELETE FROM flask_contactos WHERE id= {0}'.format(id))
    conn.commit()
    conn.close()

    flash('contacto removido exitosamente')

    return redirect(url_for('index'))

if __name__== '__main__':
    app.run(port=3000 , debug=True)
from flask import Flask, render_template, request, redirect, url_for
import os
import coneccion as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src' , 'templates')

app = Flask(__name__, static_folder='templates/assets')

@app.route('/')
def login():
    
    return render_template('pages-login.html')

@app.route('/pages-login.html')
def login2():
    
    return render_template('pages-login.html')

@app.route('/login',methods=['POST'])
def log():
    username = request.form['username']
    password = request.form['password']
    if username and password:
        cursor = db.database.cursor()
        sql = "select password from USUARIOS where USERNAME = %s"
        data = (username)
        cursor.execute(sql,(data,))
        contra = cursor.fetchall()
        passw = str(contra)
        
        return passw[3:len(passw)-4]

    

@app.route('/pages-register.html')
def registra():
    
    return render_template('pages-register.html')

@app.route('/addUsr',methods=['POST'])
def reg():
    nombre = request.form['name']
    correo = request.form['email']
    username = request.form['username']
    contra = request.form['password']

    if nombre and correo and username and contra:
        cursor = db.database.cursor()
        sql = "INSERT INTO USUARIOS (EMAIL,NOMBRE,PASSWORD,USERNAME) VALUES (%s, %s, %s, %s)"
        data = (correo,nombre,contra,username)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('login'))


@app.route('/g-students-register.html')
def home():

    return render_template('g-students-register.html')


@app.route('/g-students-grades.html')
def g_stu_grades():

    return render_template('g-students-grades.html')

@app.route('/addAlumno',methods=['POST'])
def addAlumno():
    nombre = request.form['nombre']
    aPater = request.form['aPater']
    aMater = request.form['aMater']
    boleta = request.form['boleta']
    correo = request.form['correo']
    contra = request.form['contra']
    foto = request.form['foto']

    if nombre and aPater and aMater and boleta and correo and contra:
        cursor = db.database.cursor()
        sql = "INSERT INTO ALUMNOS (NOMBRE,APATERNO,AMATERNO,BOLETA,CORREO,CONTRASENA,FOTO) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (nombre, aPater, aMater, boleta, correo, contra, foto)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=4000)
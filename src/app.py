from flask import Flask, render_template, request, redirect, url_for
import os
import coneccion as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src' , 'templates')

app = Flask(__name__, static_folder='templates/assets')


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
    if nombre and aPater and aMater and boleta and correo and contra:
        cursor = db.database.cursor()
        sql = "INSERT INTO ALUMNOS (NOMBRE,APATERNO,AMATERNO,BOLETA,CORREO,CONTRASENA) VALUES (%s, %s, %s, %s, %s, %s)"
        data = (nombre, aPater, aMater, boleta, correo, contra)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, port=4000)
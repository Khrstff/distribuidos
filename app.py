from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Lógica adicional si es necesaria para obtener datos para la página index
    return render_template('users-index.html')

@app.route('/profile')
def profile():
    # Lógica adicional si es necesaria para obtener datos del perfil
    return render_template('users-profile.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

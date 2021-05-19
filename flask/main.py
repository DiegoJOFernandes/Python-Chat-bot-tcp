from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from flask_socketio import SocketIO, emit, send


from models import User
from dao import UserDao

app = Flask(__name__)
io = SocketIO(app)

app.config.from_pyfile('config.py')

db = MySQL(app)
user_dao = UserDao(db)

messages = []



@io.on('sendMessage')
def send_message_handler(msg):
    messages.append(msg)
    emit('getMessage', msg, broadcast=True)

@io.on('message')
def message_handler(msg):
    send(messages)

@app.route("/chat")
def home():
    return render_template("chat.html")

@app.route('/inicio')
def index():
    return render_template('index.html')

@app.route('/quemsomos')
def quemsomos():
    return render_template('quemsomos.html')

  
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup', methods=['POST',])
def signup():
    name = request.form['name']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    user = User(None, name, email, username, password)
    user_dao.criar_usuario(user)
    flash('Usuário criado')
    return redirect(url_for('index'))


@app.route('/signin', methods=['POST',])
def signin():
    email = request.form['email']
    password = request.form['password']

    user = user_dao.login_usuario(email)
    if user and user.password == password:
        flash('Logado com sucesso')
        return redirect (url_for('index'))
    else:
        flash('E-mail ou senhas incorretos')
        return redirect(url_for('login'))


if __name__ == "__main__":
    io.run(app, debug=True)



app.run(debug=True)

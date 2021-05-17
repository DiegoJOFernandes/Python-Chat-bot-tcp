from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL

from models import User
from dao import UserDao

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)
user_dao = UserDao(db)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/graphic')
def graphic():
    return render_template('graphic.html')


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


@app.route('/login')
def login():
    return render_template('login.html')


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


app.run(debug=True)
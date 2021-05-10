from models import User

SQL_CRIAR_USUARIO = 'INSERT INTO users (name, email, username, password) values (%s, %s, %s, %s)'

SQL_LOGIN_USUARIO = 'SELECT id, name, email, username, password from users where email = %s'

class UserDao:
    def __init__(self, db):
        self.__db = db


    def criar_usuario(self, user):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_CRIAR_USUARIO, (user.name, user.email, user.username, user.password))
        user.id = cursor.lastrowid
        self.__db.connection.commit()
        return user
    

    def login_usuario(self, email):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_LOGIN_USUARIO, (email,))
        tupla = cursor.fetchone()
        if tupla != None:
            return User(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])


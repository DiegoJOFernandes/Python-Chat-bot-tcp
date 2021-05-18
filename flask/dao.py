from models import *

SQL_CRIAR_USUARIO = 'INSERT INTO users (name, email, username, password) values (%s, %s, %s, %s)'

SQL_LOGIN_USUARIO = 'SELECT id, name, email, username, password from users where email = %s'

SQL_OBTER_GRAFICO = 'INSERT INTO grafico (empresa, material, quantidade, cidade) values (%s, %s, %s, %s)'

SQL_PLOTAR_GRAFICO = 'SELECT empresa, material, quantidade, cidade from grafico where empresa = %s'


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


class GraficoDao:
    def __init__(self, db):
        self.__db = db

    def obter_grafico(self, grafico):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_OBTER_GRAFICO, (grafico.empresa, grafico.material, grafico.quantidade, grafico.cidade)
        grafico.empresa = cursor.lastrowid
        self.__db.connection.commit()
        return grafico

    def plotagem_grafico(self, grafico):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_PLOTAR_GRAFICO, (empresa,))
        tupla = cursor.fetchone()
        if tupla != None:
            return Grafico(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])

        def buscar_por_id(self, id):         
            cursor = self.__db.connection.cursor()         
            cursor.execute(SQL_USUARIO_POR_ID, (id,))         
            dados = cursor.fetchone()         
            usuario = traduz_usuario(dados) 
            if dados:
                else None      
                    return usuario
    


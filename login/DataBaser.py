import sqlite3

conn = sqlite3.connect('Users_data.db')

cursor = conn.cursor()
  
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(30) NOT NULL,
  email VARCHAR(45) NOT NULL,
  user VARCHAR(10) NOT NULL,
  password VARCHAR(15) NOT NULL
);
 """)

def getNameUser():
  user = cursor.execute("""
    SELECT user FROM Users
      WHERE id=(
        SELECT max(id) FROM Users)""").fetchone()
  print(user)
    

getNameUser()


print("Conectado ao Banco de Dados")
# cursor.execute(""" 
#   INSERT INTO Users values(name, email, user, password)
# """)

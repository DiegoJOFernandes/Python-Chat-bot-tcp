import MySQLdb
conn = MySQLdb.connect(user='root', passwd='root', host='127.0.0.1', port=3306)

criar_tabelas = '''
    USE aps;
    CREATE TABLE users (
      id int not null auto_increment,
      name varchar(30) not null,
      email varchar(45) not null,
      username varchar(16) not null,
      password varchar(16) not null,
      primary key (id)
    );'''

conn.cursor().execute(criar_tabelas)
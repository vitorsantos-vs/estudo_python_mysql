#importando a biblioteca pymysql
import pymysql

#criando a conexão ao servidor mysql para acesso ao banco de dados
conexao = pymysql.connect(
    host='localhost', 
    user='root',
    password= '2301',
    database='pymysql'
)

#criação do banco de dados
cursor = conexao.cursor()
cursor.execute("CREATE DATABASE pymysql")

#---------------------------------------------------------------------------------------------------------------------------------------------
#criando tabela
cursor = conexao.cursor()
cursor.execute("CREATE TABLE mysql_pessoa(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), data_nascimento DATE)")

#inserindo dados nas tabela
cursor = conexao.cursor()
con_sql = "INSERT INTO mysql_pessoa(nome, data_nascimento) VALUES(%s, %s)"
valor = [
    ('vitor', '2001-01-23'),
    ('vitor', '2001-02-23'),
    ('vitor', '2001-03-23'),
    ('vitor', '2001-04-23'),
    ('vitor', '2001-05-23'),
    ('vitor', '2001-06-23'),
    ('vitor', '2001-07-23'),
    ('vitor', '2001-08-23'),
    ('vitor', '2001-09-23'),
    ('vitor', '2001-10-23')
        ]
cursor.executemany(con_sql, valor)
conexao.commit()
print(cursor.rowcount, "inserido com sucesso")

#fazendo select na tabela
cursor = conexao.cursor()
cursor.execute("SELECT * FROM mysql_pessoa")

resultado = cursor.fetchall()

for x in resultado:
    print(x)

#---------------------------------------------------------------------------------------------------------------------------------------------
#criando tabela
cursor = conexao.cursor()
cursor.execute("CREATE TABLE mysql_endereco(id INT AUTO_INCREMENT PRIMARY KEY, rua VARCHAR(255), numero INT, cep INT)")

#inserindo dados nas tabela
cursor = conexao.cursor()
con_sql = "INSERT INTO mysql_endereco(rua, numero, cep) VALUES(%s, %s, %s)"
valor = [
    ('Rua jorge amado', 30, 2328162),
    ('Rua jorge amado', 10, 1456467),
    ('Rua jorge amado', 20, 1205267),
    ('Rua jorge amado', 20, 1234500),
    ('Rua jorge amado', 60, 5634567),
    ('Rua jorge amado', 50, 1255657),
    ('Rua jorge amado', 40, 4252215),
    ('Rua jorge amado', 80, 1289862),
    ('Rua jorge amado', 70, 1234545),
    ('Rua jorge amado', 90, 9858557)
    
        ]
cursor.executemany(con_sql, valor)
conexao.commit()
print(cursor.rowcount, "inserido com sucesso")

#fazendo select na tabela
cursor = conexao.cursor()
cursor.execute("SELECT * FROM mysql_endereco")

resultado = cursor.fetchall()

for x in resultado:
    print(x)

#---------------------------------------------------------------------------------------------------------------------------------------------
#criando tabela
cursor = conexao.cursor()
cursor.execute("CREATE TABLE mysql_trabalho(id INT AUTO_INCREMENT PRIMARY KEY, cargo VARCHAR(255), salario INT, empresa VARCHAR(255))")

#inserindo dados nas tabelas
cursor = conexao.cursor()
con_sql = "INSERT INTO mysql_trabalho(cargo, salario, empresa) VALUES(%s, %s, %s)"
valor = [
    ('Egnheiro de dados', 5000, 'Google'),
    ('Analista de sistemas', 7000, 'Microsoft'),
    ('Analista de dados', 4000, 'IBM'), 
    ('Ciêntista de dados', 8000, 'Amazon'), 
    ('Egnheiro de dados', 5000, 'Microsoft'),
    ('Analista de sistemas', 7000, 'IBM'),
    ('Analista de dados', 4000, 'Amazon'), 
    ('Ciêntista de dados', 8000, 'Google'), 
    ('Tech lider', 18000, 'Google'), 
    ('Engenheiro de software', 8000, 'Itau') 
    
        ]
cursor.executemany(con_sql, valor)
conexao.commit()
print(cursor.rowcount, "inserido com sucesso")

#fazendo select na tabela
cursor = conexao.cursor()
cursor.execute("SELECT * FROM mysql_trabalho")

resultado = cursor.fetchall()

for x in resultado:
    print(x)
    
    
#para atualizar um registro
cursor = conexao.cursor()
con_sql = "UPDATE tabela SET registro = 'xxxxx'"
cursor.execute(con_sql)
conexao.commit()

#para apagar um registro
cursor = conexao.cursor()
con_sql = "DELETE FROM tabela WHERE registro = 'xxxxx'"
cursor.execute(con_sql)
conexao.commit()

#para apagar uma tabela
cursor = conexao.cursor()
con_sql = "DROP TABLE tablea"
cursor.execute(con_sql)

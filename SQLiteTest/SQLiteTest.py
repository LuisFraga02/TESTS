import sqlite3

banco = sqlite3.connect("bancoTeste.db")

cursor = banco.cursor()

#CREATE
#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

#INSERT
#cursor.execute("INSERT INTO pessoas VALUES('maria',40,'maria123@gmail')")

#banco.commit()

cursor.execute("SELECT * FROM pessoas WHERE nome = 'maria'")
print(cursor.fetchall())
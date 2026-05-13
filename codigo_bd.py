

# formatando para POO

import sqlite3
conxao = sqlite3.connect("banco.db")
cursor = conxao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tabela_login (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               email TEXT NOT NULL,
               senha TEXT NOT NULL
               )""")

cursor.execute("""INSERT INTO tabela_login 
               (email, senha) VALUES (?, ?)
""",(dadosUsuario.email, dadosUsuario.senha))
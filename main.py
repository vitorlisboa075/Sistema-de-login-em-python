import sqlite3
from usuario import Usuario
dadadosUsuario = Usuario("", "","")
conxao = sqlite3.connect("banco.db")
cursor = conxao.cursor()

dadadosUsuario.puxarEmail()
dadadosUsuario.puxarSenha()
dadadosUsuario.mostrar()

#email= dadadosUsuarioc.puxarEmail()

quantidade = len(dadadosUsuario.senha)

if "@gmail" in dadadosUsuario.email and quantidade >= 8 :
    cursor.execute("""CREATE TABLE IF NOT EXISTS tabela_login (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               email TEXT NOT NULL,
               senha TEXT NOT NULL
               )""")

    cursor.execute("""INSERT INTO tabela_login 
               (email, senha) VALUES (?, ?)
""",(dadadosUsuario.email, dadadosUsuario.senha))
    print("login feito")
else: 
    print("email deve conter @GMAIL.COM")



conxao.commit()


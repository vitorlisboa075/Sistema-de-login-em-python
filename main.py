import sqlite3

conxao = sqlite3.connect("banco.db")
cursor = conxao.cursor()

email= input ("digite seu email")
senha = input(" digite sua senha")
quantidade = len(senha)


if "@gmail" in email and quantidade >= 8 :
    cursor.execute("""CREATE TABLE IF NOT EXISTS tabela_login (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               email TEXT NOT NULL,
               senha TEXT NOT NULL
               )""")

    cursor.execute("""INSERT INTO tabela_login 
               (email, senha) VALUES (?, ?)
""",(email, senha))
    print("login feito")
else: 
    print("email deve conter @GMAIL.COM")



conxao.commit()

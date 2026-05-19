import sqlite3
from usuario import Usuario
from codigo_bd import BancoDados
bcDados = BancoDados()
dadadosUsuario = Usuario("", "","", "")
conxao = sqlite3.connect("banco.db")
cursor = conxao.cursor()


bcDados.cadastrarEmail()




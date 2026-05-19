from usuario import Usuario
import sqlite3
class BancoDados:
    
    dadadosUsuario = Usuario('','','','')
    conxao = sqlite3.connect("banco.db")
    cursor = conxao.cursor()

    def cadastrarEmail(self, ):
      
        self.dadadosUsuario.puxarEmail()
        self.dadadosUsuario.puxarSenha()
        print(self.dadadosUsuario.email)
        quantidade = len(self.dadadosUsuario.senha)

        if "@gmail" in self.dadadosUsuario.email and quantidade >= 8 :
            BancoDados.cursor.execute("""CREATE TABLE IF NOT EXISTS tabela_login (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL
                    )""")

            BancoDados.cursor.execute("""INSERT INTO tabela_login 
                    (email, senha) VALUES (?, ?)
        """,(self.dadadosUsuario.email, self.dadadosUsuario.senha))
            print("Cadastro feito")
        else: 
            print("email deve conter @GMAIL.COM")
        BancoDados.conxao.commit()
     
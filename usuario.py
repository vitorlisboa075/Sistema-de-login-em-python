class Usuario:
    email = ""
    def __init__(self, cpf, email, senha):
        self.cpf = cpf
        self.email = email
        self.senha = senha
    
    def puxarEmail(self ):
        
        entrada = input('digite seu email')
        self.email = entrada

    def puxarSenha(self ):
        
        entrada = input('digite seu senha')
        self.senha = entrada

    
    def mostrar(self):
         print(self.email)
    

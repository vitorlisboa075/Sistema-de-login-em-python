class Usuario:
    
    def __init__(self, cpf, email, senha, id):
        self.cpf = cpf
        self.email = email
        self.senha = senha
        self.id = id
    
    def puxarEmail(self ):
        
        entrada = input('digite seu email')
        self.email = entrada
        

    def puxarSenha(self ):
        
        entrada = input('digite seu senha')
        self.senha = entrada
        

    
    def mostrar(self):
         print(self.email)
    

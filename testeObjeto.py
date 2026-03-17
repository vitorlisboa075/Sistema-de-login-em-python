class Usuario:
    def __init__(self, cpf, email, senha):
        self.cpf = cpf
        self.email = email
        self.senha = senha
    
    def verificarCPFn(self,cpf):
        if cpf == 9:
            print("cpf valido")
        elif cpf != 9:
            print("cpf invalido")





 
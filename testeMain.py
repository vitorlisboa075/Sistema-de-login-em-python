from testeObjeto import Usuario

dadosUsuario = Usuario("0732567780", "lisnoa@gmail.com","lisnaom323")
print(dadosUsuario.cpf)
print(dadosUsuario.email)
print(dadosUsuario.senha)

verificar = dadosUsuario.cpf

dadosUsuario.verificarCPFn(verificar)
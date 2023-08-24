import re

class Usuario:
    def __init__(self, senha, padrao) -> None:
        self.senha = senha 
        self.padrao = padrao
    
    def validador_senha(self):
        if re.match(self.padrao, self.senha):
            return True
        else:
            return False

padrao = r'^(?=.*[A-Z])(?=.*[!#@$%&])(?=.*[0-9])(?=.*[a-z]).{8,15}$'
s1 = input("Digite a senha: ")
usuario1 = Usuario(s1, padrao)
if usuario1.validador_senha():
    print("Senha válida!")
else:
    print("Senha inválida.")
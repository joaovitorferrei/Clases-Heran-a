import re

class Usuario:
    def __init__(self, senha) -> None:
        self.senha = senha 
        self.padrao = r'^(?=.*[A-Z])(?=.*[!#@$%&])(?=.*[0-9])(?=.*[a-z]).{8,15}$'
        self.senha_cadastrada = None
    
    def cadastro_senha(self):
        if re.match(self.padrao, self.senha):
            self.senha_cadastrada = self.senha
            return True
        else:
            return False
    
    def verificacao_senha(self, senha):
        if self.senha_cadastrada == senha:
            return True
        else:
            return False

s1 = input("Digite a senha para cadastro: ")
usuario1 = Usuario(s1)
if usuario1.cadastro_senha():
    print("Senha cadastrada com sucesso!")
else:
    print("Senha não atende aos requisitos de cadastro.")

s2 = input("Digite sua senha para verificação: ")
if usuario1.verificacao_senha(s2):
    print("Senha válida. Parabéns!")
else:
    print("Desculpe, senha não corresponde a nenhum cadastro.")

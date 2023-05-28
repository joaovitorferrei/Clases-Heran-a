class Pessoa:
    def __init__(self, nome, idade):
        if isinstance(nome, str) and isinstance(idade, int):
            self.nome = nome
            self.idade = idade
    
    def cumprimento(self):
        print(f"Olá, {self.nome}!")

    def verificacao_idade(self):
        if self.idade >= 18:
            print("Você é maior de idade.")
        else:
            print("Você é menor de idade.")

nome1 = input("Digite seu nome: ")
idade1 = int(input("Digite sua idade: "))

p1 = Pessoa(nome1, idade1)
p1.cumprimento()
p1.verificacao_idade()
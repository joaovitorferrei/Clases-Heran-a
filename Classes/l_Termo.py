# Classe Termo
class Termo:
    def __init__(self, a, i):
        self.a = a
        self.i = i

    def insere(self, outro_termo):
        self.a = outro_termo.a
        self.i = outro_termo.i

    def calcula(self, x):
        return self.a * (x ** self.i)

    def __str__(self):
        return f"{self.a}x^{self.i}"


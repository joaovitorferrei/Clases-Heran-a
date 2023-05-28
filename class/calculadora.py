class Calculadora:
    def __init__(self, num1, num2):
        if isinstance(num1, float) and isinstance(num2, float):
            self.num1 = num1
            self.num2 = num2
    
    def calcula_soma(self):
        soma = self.num1 + self.num2
        print(f"Soma: {soma:.2f}")
    
    def calcula_vezes(self):
        vezes = self.num1 * self.num2
        print(f"Vezes: {vezes:.2f}")

    def calcula_subtracao(self):
        subtracao = self.num1 - self.num2
        print(f"Subtração: {subtracao:.2f}")

    def calcula_divisao(self):
        divisao = self.num1 / self.num2
        print(f"Divisão: {divisao:.2f}")

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
calculo = Calculadora(n1, n2)
print("1 para soma") 
print("2 para multiplicação")
print("3 para subtração")
print("4 para divisão")
opcao = int(input())
if opcao <= 4:
    if opcao == 1:
        calculo.calcula_soma()
    elif opcao == 2:
        calculo.calcula_vezes()
    elif opcao == 3:
        calculo.calcula_subtracao()
    elif opcao == 4:
        calculo.calcula_divisao()
else:
    print("Você não digitou nenhuma das opções.")
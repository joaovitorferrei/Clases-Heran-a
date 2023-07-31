from Classes.__init__l import Termo,Polinomio

if __name__ == "__main__":
    # Criando termos
    termo1 = Termo(3, 2)   # 3x^2
    termo2 = Termo(5, 3)   # 5x^3
    termo3 = Termo(-2, 1)  # -2x

    # Criando polinômios
    polinomio1 = Polinomio(termo1)
    polinomio2 = Polinomio(termo2)

    # Inserindo termos nos polinômios
    polinomio1.insere(termo3)
    polinomio2.insere(Termo(4, 3))  # 4x^3

    print("Polinômio 1:", polinomio1)
    print("Polinômio 2:", polinomio2)

    # Calculando os polinômios em x = 2
    x = 2
    print(f"Valor do Polinômio 1 para x = {x}: {polinomio1.calcula(x)}")
    print(f"Valor do Polinômio 2 para x = {x}: {polinomio2.calcula(x)}")

    # Fusão dos polinômios
    polinomio1.fusao(polinomio2)
    print("Após a fusão dos polinômios:", polinomio1)

from Classes.__init__f import Ingresso, Cliente_Normal, Vip, CamaroteInferior, CamaroteSuperior

if __name__ == "__main__":
    # Classe Ingresso
    i1 = Ingresso(50)
    i1.display()

    # Classe Cliente_Normal
    c1 = Cliente_Normal(50)
    c1.display()

    # Classe Vip
    h = Vip(50)
    h.display()

    # Classe CamaroteInferior
    t = CamaroteInferior(50, 50)
    t.display()
    print(t.display_location())

    # Classe CamaroteSuperior
    b = CamaroteSuperior(50)
    b.display()

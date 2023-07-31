from .l_Termo import Termo
class Polinomio:
    def __init__(self, termo_inicial):
        self.termos = [termo_inicial]

    def insere(self, termo):
        indice_existe = -1
        for i, t in enumerate(self.termos):
            if t.i == termo.i:
                indice_existe = i
                break

        if indice_existe != -1:
            self.termos[indice_existe].a += termo.a
        else:
            self.termos.append(termo)

    def calcula(self, x):
        result = 0
        for termo in self.termos:
            result += termo.calcula(x)
        return result

    def fusao(self, outro_polinomio):
        for termo in outro_polinomio.termos:
            self.insere(termo)

    def __str__(self):
        polinomio_str = ""
        for i, termo in enumerate(self.termos):
            if i > 0:
                polinomio_str += " + "
            polinomio_str += str(termo)
        return polinomio_str


from Classes.Pessoa_4 import Pessoa,Rico,Pobre,Mendiga
if __name__=="__main__":
    #class input da Pessoa 
    p1 = Pessoa("NALDO",41)
    p1.display()
    #input do Rico
    r1 = Rico("joao",65,5300.25)
    print(r1.fazCompras())
    #input pobre
    p1 = Pobre("Marcio",19)
    print(p1.trabalha())
    #input mendigo
    m1 = Mendiga("Gustavo",15)
    m1.mendiga()
    
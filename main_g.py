from Classes.__init__g import Imovel,Novo,Velho
if __name__ == "__main__":
    imovel = Imovel("Rua A, 123", 500000)
    imovel.display_info()
    print()
    
    novo = Novo("Rua B, 456", 700000, 20000)
    novo.display_info()
    print()
    
    velho = Velho("Rua C, 789", 400000, 30000)
    velho.display_info()
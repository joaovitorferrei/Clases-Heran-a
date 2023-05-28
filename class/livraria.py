# Implemente uma classe chamada "Livro" com os atributos "título", "autor" e "ano".
# Adicione um método para exibir as informações do livro.
class Livro:
    def __init__(self,titulo,autor,ano):
        if isinstance(titulo,str) and isinstance(autor,str) and isinstance(ano,str):
            self.titulo = titulo
            self.autor = autor
            self.ano = ano
    def informacoes_livro(self):
        print(f"titulo: {self.titulo}")
        print(f"autor: {self.autor}")
        print(f"ano: {self.ano}")

t1 = "senhor dos aneis"
a1 = "J. R. R. Tolkien"
ano1 = "1954" #escolhi o ano como string porque em um projeto maior colocar um número
l1 = Livro(t1,a1,ano1)# inteiro ia gastar muita memoria
l1.informacoes_livro()


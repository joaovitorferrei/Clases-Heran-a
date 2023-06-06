# Crie uma classe chamada Livro que tenha os atributos titulo, autor e num_paginas. 
# Crie métodos
# emprestar e devolver que mudam o estado do livro para emprestado e não emprestado,
# respectivamente.
class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            print(f"O livro '{self.titulo}' foi emprestado.")
        else:
            print(f"O livro '{self.titulo}' já está emprestado.")

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            print(f"O livro '{self.titulo}' foi devolvido.")
        else:
            print(f"O livro '{self.titulo}' já está disponível.")


livro1 = Livro("Dom Quixote", "Miguel de Cervantes", 863)
livro1.emprestar()  # Empréstimo bem-sucedido
livro1.devolver()  # Devolução bem-sucedida
livro1.devolver()  # Tentativa de devolução quando o livro já está disponível
livro1.emprestar()  # Tentativa de empréstimo quando o livro já está emprestado

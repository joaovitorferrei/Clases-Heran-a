# Escreva uma classe cujos objetos representam alunos matriculados em uma disciplina. Cada
# objeto dessa classe deve guardar os seguintes dados do aluno: matrícula, nome, 2 
# notas de prova e 1 nota de trabalho. Escreva os seguintes métodos para esta classe:
# a) media calcula a média final do aluno (cada prova tem peso 2,5 e o trabalho tem peso 2)
# b) final calcula quanto o aluno precisa para a prova final (retorna zero se ele não for para a
# final)
class Aluno:
    def __init__(self, nome, matricula, disciplina):
        self.__nome = nome
        self.__matricula = matricula
        self.__disciplina = disciplina
        self.__prova = []
        self.__trabalho = None
        self.__media_final = None

    def calcular_media(self):
        peso_provas = 2.5
        peso_trabalho = 2

        for i in range(2):  # Loop para receber as duas notas da prova
            nota = float(input("Digite a nota da prova: "))
            self.__prova.append(nota)  # Adiciona a nota à lista de provas

        self.__trabalho = float(input("Digite a nota do trabalho: "))

        # Cálculo da média final
        self.__media_final = (sum(self.__prova) * peso_provas + self.__trabalho * peso_trabalho) / (peso_provas * 2 + peso_trabalho)
        print("-"*30)
    def exibir_informacoes(self):
        print("Nome:", self.__nome)
        print("Matrícula:", self.__matricula)
        print("Disciplina:", self.__disciplina)
        print("Nota da Prova:", self.__prova)
        print("Nota do Trabalho:", self.__trabalho)
        print(f"Média Final: {self.__media_final:.2f}")


# Exemplo de uso da classe Aluno
aluno1 = Aluno("João", 123, "Matemática")
aluno1.calcular_media()
aluno1.exibir_informacoes()

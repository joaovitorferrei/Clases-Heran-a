from Classes.Funcionario_3 import Funcionario, Assistente, Administrativo,Tecnico
# Exercício 1: Implemente a classe Funcionario com nome, salario e os métodos
# addAumento(double valor), ganhoAnual() e exibeDados() - imprime os valores do funcionário.
# a. crie a classe Assistente, que também é um funcionário, e que possui um número de
# matrícula (faça os métodos GET e SET). Sobrescreva o método exibeDados().
# b. sabendo que os Assistentes Técnicos possuem um bônus salarial e que os Assistentes
# Administrativos possuem um turno (dia ou noite) e um adicional noturno, crie as classes
# Tecnico e Administrativo e sobrescreva o método ganhoAnual() de ambas as classes
# (Administrativo e Tecnico)
tecnico = Tecnico("João", 2000.0, "1234", "Noturno")
tecnico.set_adicional_noturno(500.0)
tecnico.exibir_dados()
print()
assistente = Assistente("Maria", 1500.0, "5678")

# Exibindo os dados do assistente
assistente.exibir_dados()
print()
# Criando um objeto Administrativo com turno dia e sem adicional noturno
administrativo = Administrativo("Guilherme", 2000.0, "1234", "Dia")

# Exibindo os dados do administrativo
administrativo.exibir_dados()


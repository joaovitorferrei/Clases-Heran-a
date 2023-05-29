# 1 PARTE DO PROGRAMA
# Crie uma classe chamada "ContaBancaria" com os seguintes atributos privados:
# __titular (string): nome do titular da conta.
# __saldo (float): saldo atual da conta.
# A classe deve ter os seguintes métodos públicos:

# depositar(valor: float): adiciona o valor especificado ao saldo da conta.
# sacar(valor: float): retira o valor especificado do saldo da conta, desde que haja saldo 
# suficiente. Caso contrário, exibe uma mensagem de erro.
# obter_saldo() -> float: retorna o saldo atual da conta.
# exibir_informacoes(): exibe as informações da conta, incluindo o titular e o saldo.
#=======================================================================================
# 2 PARTE DO PROGRAMA
#Crie uma classe chamada "ContaPoupanca" que herda da classe "ContaBancaria". 
# Essa classe deve adicionar um atributo privado adicional:
#__juros (float): taxa de juros aplicada sobre o saldo da conta poupança.
#A classe ContaPoupanca deve ter os seguintes métodos públicos:
# calcular_juros(): calcula e adiciona os juros ao saldo da conta poupança com base 
# na taxa de juros definida.
# exibir_informacoes(): sobrescreve o método exibir_informacoes() da classe pai 
# para exibir também a taxa de juros.
# A ideia é simular um sistema bancário simples com contas bancárias e contas
# poupança, onde é possível depositar, 
# sacar, obter saldo e calcular juros em uma conta poupança.
class Conta_bancaria:
    def __init__(self, titular, saldo):
        if isinstance(saldo, float):
            self.__saldo = saldo
            self.__titular = titular

    def depositar(self, valor):
        self.__saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente. Tente um valor menor.")

    def obter_saldo(self):
        return self.__saldo

    def exibir_informacoes(self):
        print(f"Titular: {self.__titular}")
        print(f"Seu saldo atual é R$ {self.__saldo:.2f}")

#-------------------------------------------------------------------------------------------
class ContaPoupanca(Conta_bancaria):
    def __init__(self, titular, saldo, juros):
        super().__init__(titular, saldo)
        if isinstance(juros, float):
            self.__juros = juros

    def calcular_juros(self):
        juros = self.obter_saldo() * self.__juros
        self.depositar(juros)
        print(f"Juros de R$ {juros:.2f} calculados e adicionados ao saldo.")

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Taxa de juros: {self.__juros * 100}%")

# Criando uma instância da classe ContaPoupanca
conta_poupanca = ContaPoupanca("Joao vitor", 1000.0, 0.05)
# -------------------------------exibindo-informacoes---------------------------------------------
# Realizando um depósito
conta_poupanca.depositar(500.0)

# Realizando um saque
conta_poupanca.sacar(200.0)

# Obtendo o saldo atual
saldo_atual = conta_poupanca.obter_saldo()
print(f"Saldo atual: R$ {saldo_atual:.2f}")

# Calculando os juros da conta poupança
conta_poupanca.calcular_juros()

# Obtendo o saldo atual após o cálculo dos juros
saldo_atualizado = conta_poupanca.obter_saldo()
print(f"Saldo após juros: R$ {saldo_atualizado:.2f}")

# Exibindo as informações da conta poupança
conta_poupanca.exibir_informacoes()

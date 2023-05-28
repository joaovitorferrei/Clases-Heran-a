# Crie uma classe chamada "Banco" com o atributo "saldo" e métodos para 
# depositar e sacar dinheiro. Adicione um método para exibir o saldo atual
class Banco:
    def __init__(self,saldo):
        if isinstance(saldo,float):
            self.saldo = 0
    def deposito_conta(self,valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
    def sacar_dinheiro(self,valor):
        if  valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("saldo insuficiente tente um saldo menor")
    def exibir_saldo(self):
        print(f"seu saldo: {self.saldo:.2f}")

# Criando uma instância da classe Banco
conta = Banco(1000.0)

# Interagindo com o usuário para realizar um depósito
valor_deposito = float(input("Digite o valor do depósito: "))
conta.deposito_conta(valor_deposito)

# Interagindo com o usuário para realizar um saque
valor_saque = float(input("Digite o valor do saque: "))
conta.sacar_dinheiro(valor_saque)

# Exibindo o saldo atual
conta.exibir_saldo()

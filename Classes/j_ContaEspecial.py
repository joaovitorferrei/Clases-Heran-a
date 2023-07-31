from .j_ContaCorente import ContaCorrente

# Classe ContaEspecial (Herda de ContaCorrente)
class ContaEspecial(ContaCorrente):
    def __init__(self, numero_conta, titular, saldo, limite):
        super().__init__(numero_conta, titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        limite_disponivel = self._saldo + self.limite
        if valor <= limite_disponivel:
            if valor <= self._saldo:
                self._saldo -= valor
            else:
                # Se o valor for maior que o saldo, calculamos o saque usando o limite
                saque_limite = valor - self._saldo
                self._saldo = 0
                self.limite -= saque_limite
            return True
        return False


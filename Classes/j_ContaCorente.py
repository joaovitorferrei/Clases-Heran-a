class ContaCorrente:
    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self._saldo = saldo

    def get_saldo(self):
        return self._saldo

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            return True
        return False


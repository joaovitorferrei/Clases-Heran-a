from Classes.__init__j import ContaCorrente,ContaEspecial
# Teste das classes
if __name__ == "__main__":
    conta1 = ContaEspecial("1234", "João", 1000, 500)
    print(f"Saldo inicial: {conta1.get_saldo()}")

    # Teste de saque
    saque_valor = 1200
    if conta1.sacar(saque_valor):
        print(f"Saque de {saque_valor} realizado. Novo saldo: {conta1.get_saldo()}, Limite restante: {conta1.limite}")
    else:
        print(f"Saque de {saque_valor} não autorizado. Saldo + Limite disponível: {conta1.get_saldo() + conta1.limite}")
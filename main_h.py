from Classes.__init__h import Gerente,Vendedor
if __name__ == "__main__":
    gerente = Gerente("João", 5000.0)
    gerente.salario = 6000.0
    print(gerente)  # Saída: Nome: João, Salário: 6000.0

    vendedor = Vendedor("Maria", 3000.0, 10)
    vendedor.percentual_comissao = 15
    print(vendedor)  # Saída: Nome: Maria, Salário sem comissão: 3000.0, Salário com comissão: 3450.0, Percentual de comissão: 15%

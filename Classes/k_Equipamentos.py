class Equipamento:
    def __init__(self, num_equipamentos):
        self.num_equipamentos = num_equipamentos
        self.valores = [0] * num_equipamentos

    def get_numero_equipamentos(self):
        return self.num_equipamentos

    def get_valor(self, equipamento):
        return self.valores[equipamento]

    def set_valor(self, equipamento, valor):
        self.valores[equipamento] = valor


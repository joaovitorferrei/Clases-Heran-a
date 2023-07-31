from .k_Equipamentos import Equipamento
# Classe EquipamentoCorrigido (Herda de Equipamento)
class EquipamentoCorrigido(Equipamento):
    def __init__(self, num_equipamentos):
        super().__init__(num_equipamentos)
        self.mes_compra = [0] * num_equipamentos

    def registrar_mes_compra(self, equipamento, mes_compra):
        self.mes_compra[equipamento] = mes_compra

    def corrigir_valor(self, equipamento, fator_correcao):
        if self.mes_compra[equipamento] == 12:  # Se o equipamento foi comprado em dezembro, corrigir o valor
            valor_corrigido = self.valores[equipamento] * fator_correcao
            self.valores[equipamento] = valor_corrigido

    # Método toString
    def __str__(self):
        output = "Equipamentos com valores corrigidos:\n"
        for i in range(self.num_equipamentos):
            output += f"Equipamento {i}, Valor: {self.valores[i]}, Mês de Compra: {self.mes_compra[i]}\n"
        return output


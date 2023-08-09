from Classes.__init__k import Equipamento,EquipamentoCorrigido
# Teste das classes
if __name__ == "__main__":
    equipamentos = 5
    equipamentos_corrigidos = EquipamentoCorrigido(equipamentos)

    # Setar valores para os equipamentos
    for i in range(equipamentos):
        equipamentos_corrigidos.set_valor(i, (i + 1) * 1000)

    # Registrar os meses de compra
    equipamentos_corrigidos.registrar_mes_compra(0, 3)  # Equipamento 0 foi comprado em março
    equipamentos_corrigidos.registrar_mes_compra(1, 8)  # Equipamento 1 foi comprado em agosto
    equipamentos_corrigidos.registrar_mes_compra(2, 12)  # Equipamento 2 foi comprado em dezembro
    equipamentos_corrigidos.registrar_mes_compra(3, 5)  # Equipamento 3 foi comprado em maio
    equipamentos_corrigidos.registrar_mes_compra(4, 11)  # Equipamento 4 foi comprado em novembro

    print(equipamentos_corrigidos)

    # Corrigir os valores dos equipamentos comprados em dezembro com um fator de correção de 1.05 (5% de aumento)
    for i in range(equipamentos):
        equipamentos_corrigidos.corrigir_valor(i, 1.05)

    print("Após a correção dos valores:\n")
    print(equipamentos_corrigidos)
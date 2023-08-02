from datetime import datetime
# data_str_data = "2022-04-20 07:49:23"
# data_str_fmt = "%Y-%m-%d %H:%M:%S"
# data = datetime.strptime(data_str_data,data_str_fmt)
# print(data)

#daqui ate os trasos ele pega a date real do computador e covert diretamente para br
data_atual = datetime.now()

# Formatação da data
data_form = data_atual.strftime('%d/%m/%Y')

print(data_form)
# --------------------------------------

# dessa linha para baixo isso coverte uma data que e america para data brasileiraclea
data_str = '07/07/2023'

# Conversão da string para datetime
data_objeto = datetime.strptime(data_str, '%d/%m/%Y')

# Formatação da data
data_formatada = data_objeto.strftime('%d/%m/%Y')

print(data_formatada)
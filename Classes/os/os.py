import os

# mudando de pasta para outra
# novo_caminho = r'c:/Users/PARTICULAR/Downloads'
# os.chdir(novo_caminho)
# print(f'meu novo cominho: {novo_caminho} \n')|

# saber o caminho que voce esta no momento
# print(os.getcwd())|

# cria uma um arquivo
# os.mkdir('Teste')|

# lista os arquivos dentro 
# print(os.listdir())|

# criando mais de uma pasta em entrando no pasta
# exemplo: Dowloads\2023\21\manha significa que 2023 esta dentro de Dowlads e dentro 2023 tem o dia 21 e dentro do dia 21 tem amanha|
# caminho = r'c:\Users\PARTICULAR\Downloads\2023\21\manhã'
# os.makedirs(caminho)
# print(os.listdir())

# so permite apagar pastas vazias
# os.rmdir(r'c:\Users\PARTICULAR\Downloads\2023\21\manhã')|

# abrir um arquivo
# os.startfile(r'c:\Users\PARTICULAR\Downloads\2023\21\text.txt')

# renomear arquivos
# os.getcwd()
# print('\n')
# os.chdir(r'c:\Users\PARTICULAR\Downloads\2023\21')
# os.rename('velho.txt','novo.txt')
# os.listdir()

# remover um arquivo
# os.getcwd()
# os.chdir(r'c:\Users\PARTICULAR\Downloads\2023\21')
# os.remove('novo.txt')

# concatenar de forma sem erro um conjunto de palavras
# drive = 'C:'
# usuario = 'PARTICULAR'
# pasta_base = 'Downloads'
# caminho = os.path.join(drive,r'\Users',usuario,'Desktop',pasta_base) 
# print(caminho)
# print(os.getcwd())
import re

string = "teste de expreçoes regulares teste."
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste','abcd', string))
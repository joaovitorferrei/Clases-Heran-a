class Agenda:
    def __init__(self):
        self.__contatos = {}

    def adicionar_contato(self, nome, telefone):
        if nome in self.__contatos:
            self.__contatos[nome].append(telefone)
        else:
            self.__contatos[nome] = [telefone]

    def excluir_telefone(self, nome, telefone):
        if nome in self.__contatos and telefone in self.__contatos[nome]:
            self.__contatos[nome].remove(telefone)
            print("Telefone removido com sucesso!")
        else:
            print("Telefone não encontrado.")

    def obter_contatos(self):
        return self.__contatos


agenda = Agenda()
continuar = True

while continuar:
    print("Digite 1 para acrecentar um contato")
    print("Digite 2 para excluir um telefone")
    print("Digite 3 para parar")
    opcao = int(input())

    if opcao == 1:
        print("Adicionando contato...")
        nome_contato = input("Digite o nome do contato: ")
        telefone_contato = input("Digite o número de telefone do contato: ")
        agenda.adicionar_contato(nome_contato, telefone_contato)
    elif opcao == 2:
        print("Excluindo telefone...")
        nome_contato = input("Digite o nome do contato: ")
        telefone_contato = input("Digite o número de telefone a ser excluído: ")
        agenda.excluir_telefone(nome_contato, telefone_contato)
    elif opcao == 3:
        print("Parando o programa...")
        continuar = False
    else:
        print("Opção inválida. Digite novamente.")

print("Contatos adicionados:")
for nome, telefones in agenda.obter_contatos().items():
    print(f"Nome: {nome}")
    print("Telefones:")
    for telefone in telefones:
        print(telefone)
    print()

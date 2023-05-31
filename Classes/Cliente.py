class Cliente:
    def __init__(self,nome,endereco=None) -> None:
        self.nome = nome
        self.endereco = endereco
    def obterClasseCredito()->str:
        return "Boa"
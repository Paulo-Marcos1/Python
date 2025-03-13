class Aluno:

    def __init__(self, nome: str, idade:int, notas: list[float]) -> None:
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media(self:object) ->float:
        
        return sum(self.notas) / len(self.notas)

from typing import List, Dict

class Aluno:
    """
    Representa um aluno com nome e nota

    Atributos:
        nome (str): Nome do aluno
        nota (float): Nota do aluno
    """
    def __init__(self, nome: str, nota: float):
        """
        Inicializa uma nova instância de Aluno.

        Args:
        nome (str): Nome do aluno
        nota (float): Nota do aluno
        """
        self.nome = nome.strip().title()
        self.nota = float(nota)

    def to_dict(self) -> Dict[str, float]:
        """
        Retorna o aluno como um dicionario com nome e nota.

        returns:
            dict Um dicionario {nome: nota}
        """
        return {self.nome: self.nota}

    def __str__(self) -> str:
        """
        Representação em string do aluno formato CSV

        returns:
        str: Nome e nota separados por virgula.

        """
        return f"{self.nome}, {self.nota:.1f}"

from pathlib import Path
from GerenciadorAlunos import GerenciadorAlunos
from Aluno import Aluno


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    gerenciador = GerenciadorAlunos(base_dir)

    print("Cadastrado:", gerenciador.cadastrar(Aluno("Paulo", 7)))
    print("Lendo:", gerenciador.buscar("Paulo"))
    print("Lista completa:", gerenciador.listar())
    print("Removendo: ", gerenciador.remover("Paulo"))
    print("Lista pos remoção: ", gerenciador.listar())
    print("Novo cadastro: ", gerenciador.cadastrar(Aluno("Maria", 7)))
    print("Alterando nota:", gerenciador.alterar_nota("Maria", 10))
    print("Lista final:", gerenciador.listar())

from aluno import Aluno

if __name__ == '__main__':
    aluno1 = Aluno("Paulo", 24,[4.5,7.4,8.3,6.8])
    aluno2 = Aluno("Mario", 22,[2, 8, 7.2, 6])
    
    alunos = [aluno1, aluno2]

    for aluno in alunos:
        if aluno.calcular_media() >= 6:
            print(f"Aluno: {aluno.nome} \nMédia: {aluno.calcular_media()} \nAprovado\n-----------------")
        else:
            print(f"Aluno: {aluno.nome} \nMédia: {aluno.calcular_media()} \nReprovado\n-----------------")

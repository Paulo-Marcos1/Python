def escrever_aluno():
   nome = str(input("Digite o nome do Aluno: "))
   n1 = float(input("Digite a primeira nota: "))
   n2 = float(input("Digite a segunda nota: "))
   media = (n1 + n2)/2
   dados = f"Aluno: {nome} \n1ª Prova:{n1} \n2ª Prova:{n2} \nMedia:{media}\n\n"

   caminho = open("Alunos.txt", "a", encoding="utf-8")
   caminho.write(dados)
   caminho.close()

escrever_aluno()

import random
num_secreto= random.randint(1,100)
contador = 0
while True:
    tentativa = int(input("Adivinhe o numero de 1 a 100: \n"))
    contador = contador + 1
    if contador == 8:
        print("Você perdeu o numero era:",num_secreto)
        break
    if tentativa > num_secreto:
        print("Tente um numero menor")
    elif tentativa < num_secreto:
        print("Tente um numero maior")
    else:
        print("Você acertou o numero")
        break
    print("Você tentou ",contador,(" vezes!"))

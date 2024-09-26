import random
acerto = 0
contmax=0
for i in range(0,100):
    num_secreto= random.randint(1,100)
    contador = 0
    print("Voce tentou 1 vez!")
    minimo = 1
    maximo = 100
    tentativa = random.randint(1,100)
    while True:
        contador = contador + 1
        contmax = contmax + 1
        print(tentativa)
        if contador == 7 and tentativa != num_secreto :
            print("Você perdeu o numero era:",num_secreto)
            break
        if tentativa > num_secreto:
            print("Tente um numero menor")
            maximo = tentativa - 1
        elif tentativa < num_secreto:
            print("Tente um numero maior")
            minimo = tentativa + 1
        else:
            print("Você acertou o numero")
            break
        print("Você tentou ",contador+1,(" vezes!"))
        tentativa = (minimo + maximo)//2
        if tentativa == num_secreto:
            acerto=acerto + 1
contmax = contmax / 100
print("A taxa de acerto foi de:",acerto,"%")
print("em ",contmax," tentativas")

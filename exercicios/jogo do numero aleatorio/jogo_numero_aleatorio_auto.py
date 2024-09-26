import random
import time


num_secreto= random.randint(1,100)
contador = 0
print("Voce tentou 1 vez!")
minimo = 1
maximo = 100
tentativa = random.randint(1,100)
while True:
    time.sleep(1)
    contador = contador + 1
    print(tentativa)
    if contador == 8 and tentativa != num_secreto :
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
        num_secreto =random.randint(1,100)
        break
    print("Você tentou ",contador+1,(" vezes!"))
    tentativa = (minimo + maximo)//2
        

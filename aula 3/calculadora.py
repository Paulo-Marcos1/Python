import time
def menu():
    print("-"*30)
    print("Escolha uma operacao")
    print("\n1-Soma")
    print("\n2-Subtracao")
    print("\n3-Divisao")
    print("\n4-multiplicacao")
    print("\n0-Sair")
    print("-"*30)
    escolha = int(input("Digite sua escolha:")) 
    return escolha
def soma ():
    a = float(input("Digite o primeiro numero da soma:"))
    b = float(input("Digite o segundo numero da soma:"))
    n = a + b
    print(f"O resultado foi:{n}")
    return

def subtracao():
    a = float(input("Digite o primeiro numero da subtracao:"))
    b = float(input("Digite o segundo numero da subtracao:"))
    n = a - b
    print(f"O resultado foi:{n}")
    return

def divisao():
    a = float(input("Digite o dividendo:"))
    b = float(input("Digite o divisor:"))
    n = a / b
    print(f"O resultado foi {n}")
    return 

def multiplicacao():
    a = float(input("Digite o primeiro numero da multiplicacao:"))
    b = float(input("digite o segundo numero da multiplicacao:"))
    n = a * b
    print(f"O resultado foi:{n}")
    return

while True:
    escolha = menu()
    if(escolha == 1):
        soma()
    elif (escolha == 2):
        subtracao()
    elif (escolha == 3):
        divisao()
    elif (escolha == 4):
        multiplicacao()
    elif (escolha == 0):
        print("saindo........")
        break
    else:
        print("numero invalido tente novamente\n")
        print("-"*30)
    time.sleep(1)
    

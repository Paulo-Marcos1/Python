palavra_secreta = 'perfume'
letra_acertada = ''
tentativas_max = len(palavra_secreta) + 6
tentativas = 0 
while True:

    letra_digitada = input('Digite uma letra:')
    tentativas += 1
    if len (letra_digitada)> 1:
        print('Digite apenas uma letra!')
        tentativas -=1
        continue
    elif len (letra_digitada) < 1:
        print('Digite uma letra!')
        tentativas -= 1
        continue

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(palavra_formada)
    print(f'\n{tentativas} tentativas de {tentativas_max} possiveis')
    if tentativas == tentativas_max +1:
        print(f'Acabou suas tentativas a palavra secreta era {palavra_secreta}. ')
        break
    elif palavra_formada == palavra_secreta:
        print('ta certo')
        break
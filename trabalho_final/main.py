
palavras = ['DADOS', 'DESVIO', 'MEDIA']  # Palavras apenas para teste
perdeu = False


def forca(palavra, chances):
    while True:
        for letra in palavra:
            if letra in letras_tentadas:
                print(letra, end=' ')
            else:
                print('_', end=' ')

        tentativa = input('\n\nDigite uma letra: ').upper()

        if len(tentativa) > 1:
            print('Digite apenas uma letra!')
            continue
        if tentativa.isdigit():
            print('Digite apenas letras!')
            continue

        letras_tentadas.add(tentativa)
        if tentativa not in palavra:
            chances -= 1
            print(f'Você tem {chances} chances')

        ganhou = True
        for letra in palavra:
            if letra not in letras_tentadas:
                ganhou = False

        if chances == 0:
            global perdeu
            perdeu = True
            break

        if ganhou:
            break

    if ganhou:
        print(f'\nAcertou! A palavra é {palavra}')

    else:
        print(f'\nPerdeu! A palavra era {palavra}')


for i, palavra in enumerate(palavras, start=1):
    letras_tentadas = []
    letras_tentadas = set(letras_tentadas)
    chances = 5  # esta variável será trocada pelo atributo jogador.chances
    ganhou = True

    print(f'\n\nRodada {i}'.center(50))
    forca(palavra, chances)
    if perdeu:
        print(f'Jogo encerrado! Você jogou {i} rodadas')
        break

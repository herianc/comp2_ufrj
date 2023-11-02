# logica do jogo da forca que será importada para o arquivo main.py

def forca(palavra, chances, pontos) -> bool:
    letras_tentadas = []
    # Usando a estrutura de dados Set para eliminar repetições
    letras_tentadas = set(letras_tentadas)

    while True:
        for letra in palavra:
            if letra in letras_tentadas:
                print(letra, end=' ')
            else:
                print('_', end=' ')

        tentativa = input('\n\nLetra: ').upper()

        # Tratando os erros de entrada
        if len(tentativa) > 1:
            print('Digite apenas uma letra!')
            continue
        if tentativa.isdigit():
            print('Digite apenas letras!')
            continue

        letras_tentadas.add(tentativa)
        if tentativa not in palavra:
            chances -= 1
            pontos -= pontos/10
            print(f'Você perdeu uma chance. {chances} chances restantes')

        ganhou = True
        for letra in palavra:
            if letra not in letras_tentadas:
                ganhou = False

        if chances == 0:
            print(f'\nPerdeu! A palavra era {palavra}')
            pontos = 0
            return ganhou, pontos

        if ganhou:
            print(f'\nAcertou! A palavra é {palavra}')
            return ganhou, pontos

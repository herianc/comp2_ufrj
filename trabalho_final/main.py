from forca import forca

palavras = ['DADOS', 'DESVIO', 'MEDIA']  # Palavras apenas para teste
perdeu = False


for i, palavra in enumerate(palavras, start=1):
    chances = 3  # esta variável será trocada pelo atributo jogador.chances

    print(f'\n\nRodada {i}'.center(50))
    perdeu = forca(palavra, chances)

    if perdeu:
        print(f'Jogo encerrado! Você jogou {i} rodadas')
        break

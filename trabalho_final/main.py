import classes
from os import system
pts = 0


escolha = input(
    'JOGO DA FORCA - MENU\n1 - Estatística\n2 - Geociências\n3 - Sair\n')

match escolha:
    case '1':
        jogo = classes.Estatistica()

        resultado = jogo.nivel_facil()
        pts += resultado[1]

        if resultado[0]:
            resultado = jogo.nivel_medio()
            pts += resultado[1]

        if resultado[0]:
            resultado = jogo.nivel_dificil()
            pts += resultado[1]

    case '2':
        jogo = classes.Geociencias()

        resultado = jogo.nivel_facil()
        pts += resultado[1]

        if resultado[0]:
            resultado = jogo.nivel_medio()
            pts += resultado[1]

        if resultado[0]:
            resultado = jogo.nivel_dificil()
            pts += resultado[1]
    case '3':
        pass
    case _:
        print('Entrada inválida!')

nome = input('\n\nDigite o seu nome: ').upper().strip()

if pts != 0:
    jogador = classes.Jogador(nome)
    jogador.adicionar_pontuacao(pts)

    with open('pontuacao.txt', 'a') as arquivo:
        arquivo.write(
            f'\nJOGADOR: {jogador.nome} - {jogador.pontuacao:.2f} PTS')

system('cls')
# fazer funções que armazenem e mostrem a pontuação no arquivo.
with open('pontuacao.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha, end='')

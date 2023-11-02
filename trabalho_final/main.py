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
    case _:
        print('Entrada inválida!')


nome = input('\n\nDigite o seu nome: ')

jogador = classes.Jogador(nome)
jogador.adicionar_pontuacao(pts)

system('cls')
print('PONTUAÇÃO FINAL'.center(50, '-'))
print(f'JOGADOR: {jogador.nome} - {jogador.pontuacao} PTS')

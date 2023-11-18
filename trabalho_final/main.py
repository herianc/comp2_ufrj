import classes
import forca
from os import system
pts = 0

system('cls')
escolha = input(
    'JOGO DA FORCA - MENU\n1 - Estatística\n2 - Geociências\n3 - Sair\n')

match escolha:
    case '1':
        jogo = classes.Estatistica()

        resultado = jogo.nivel_facil()
        pts += resultado[1]

        if resultado[0]:
            # PASSOU PARA O NÍVEL MÉDIO
            # forca.tocar_som('trabalho_final\sounds\win_level.wav')
            resultado = jogo.nivel_medio()
            pts += resultado[1]
        else:
            ...
            # forca.tocar_som('trabalho_final\sounds\lose.wav')

        if resultado[0]:
            # PASSOU PARA O NÍVEL DIFICIL
            # forca.tocar_som('trabalho_final\sounds\win_level.wav')
            resultado = jogo.nivel_dificil()
            pts += resultado[1]
        else:
            ...
            # forca.tocar_som('trabalho_final\sounds\lose.wav')

    case '2':
        jogo = classes.Geociencias()

        resultado = jogo.nivel_facil()
        pts += resultado[1]

        if resultado[0]:
            # PASSOU PARA O NÍVEL MEDIO
            # forca.tocar_som('trabalho_final\sounds\win_level.wav')
            resultado = jogo.nivel_medio()
            pts += resultado[1]
        else:
            ...
            # forca.tocar_som('trabalho_final\sounds\lose.wav')

        if resultado[0]:
            # PASSOU PARA O NÍVEL DIFICIL
            # forca.tocar_som('trabalho_final\sounds\win_level.wav')
            resultado = jogo.nivel_dificil()
            pts += resultado[1]

        else:
            ...
            # forca.tocar_som('trabalho_final\sounds\lose.wav')

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
            f'\n{jogador.nome} - {jogador.pontuacao:.2f} PTS')

system('cls')
# fazer funções que armazenem e mostrem a pontuação no arquivo.

try:
    with open('pontuacao.txt', 'r') as arquivo:
        classificao = ''
        for linha in arquivo.readlines():
            classificao += linha
except FileNotFoundError:
    print('ARQUIVO NÃO ENCONTRADO')
except:
    print('ERRO DESCONHECIDO')

print(classificao)

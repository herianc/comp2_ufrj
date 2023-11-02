from classes import Estatistica, Geociencias
pts = 0


est = Estatistica()

resultado = est.nivel_facil()
pts += resultado[1]

if resultado[0]:
    resultado = est.nivel_medio()
    pts += resultado[1]

if resultado[0]:
    resultado = est.nivel_dificil()
    pts += resultado[1]

print(f'A pontuação final é: {pts}')

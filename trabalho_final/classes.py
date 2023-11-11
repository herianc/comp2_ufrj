from abc import ABC, abstractclassmethod
from forca import forca
import random
from os import system
from time import sleep

# Classes que serão importadas para o arquivo main.py e será molde para os temas do jogo e instanciação do jogador


class Tema(ABC):
    # Classe Abstrata de Geociências e Estatística: fornece a estrutura das classes filhas
    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def nivel_facil(self):
        ...

    @abstractclassmethod
    def nivel_medio(self):
        ...

    @abstractclassmethod
    def nivel_dificil(self):
        ...


class Estatistica(Tema):
    # Classe para as palavras relacionadas a Estatística
    def __init__(self) -> None:
        super().__init__()
        self.palavras_faceis = ['AMOSTRA', 'VARIAVEL', 'POPULACAO', 'DADOS',
                                'DESVIO', 'MEDIANA', 'MEDIA', 'MODA', 'EVENTOS', 'GRAFICO']

        self.palavras_medias = ['PARAMETRO', 'VIES', 'ESPERANCA', 'BINOMIAL', 'INFERENCIA',
                                'ANALISE DESCRITIVA', 'QUANTIS', 'ESTIMADOR', 'AMOSTRA ALEATORIA', 'PROPORCAO']

        self.palavras_dificeis = ['HISTOGRAMA', 'PROBABILIDADE', 'REGRESSAO', 'VARIANCIA', 'DISTRIBUICAO',
                                  'POISSON', 'TEOREMA DE BAYES', 'BERNOULLI', 'COEFICIENTE DE VARIACAO', 'OUTLIERS']

    def nivel_facil(self):
        # Embaralhando a ordem das palavras
        random.shuffle(self.palavras_faceis)
        pontos_no_nivel = 0
        print('NÍVEL FÁCIL'.center(50))

        for i, palavra in enumerate(self.palavras_faceis[:3], start=1):
            system('cls')
            chances = 7
            print(f'Você tem {chances} chances')
            print(f'\n\nNível Fácil - Rodada {i}'.center(50))
            resultado = forca(palavra, chances, 250)
            pontos_no_nivel += resultado[1]

            if not resultado[0]:
                print(f'Jogo encerrado! Você jogou {i} rodadas')
                return False, pontos_no_nivel
            sleep(2)
        return True, pontos_no_nivel

    def nivel_medio(self):
       # Embaralhando a ordem das palavras
        random.shuffle(self.palavras_medias)
        pontos_no_nivel = 0
        print('NÍVEL MÉDIO'.center(50))

        for i, palavra in enumerate(self.palavras_medias[:3], start=1):
            system('cls')
            chances = 7
            print(f'Você tem {chances} chances')
            print(f'\n\nNível Médio - Rodada {i}'.center(50))
            resultado = forca(palavra, chances, 500)
            pontos_no_nivel += resultado[1]

            if not resultado[0]:
                print(f'Jogo encerrado! Você jogou {i} rodadas')
                return False, pontos_no_nivel
            sleep(2)
        return True, pontos_no_nivel

    def nivel_dificil(self):
        # Embaralhando a ordem das palavras
        random.shuffle(self.palavras_dificeis)
        pontos_no_nivel = 0
        print('NÍVEL DIFÍCIL!'.center(50))

        for i, palavra in enumerate(self.palavras_dificeis[:3], start=1):
            system('cls')
            chances = 7
            print(f'Você tem {chances} chances')
            print(f'\n\nNível Difícil - Rodada {i}'.center(50))
            resultado = forca(palavra, chances, 1000)
            pontos_no_nivel += resultado[1]

            if not resultado[0]:
                print(f'Jogo encerrado! Você jogou {i} rodadas')
                return False, pontos_no_nivel
            sleep(2)
        return True, pontos_no_nivel


class Geociencias(Tema):
    # Classe para as palavras relacionadas ao BCMT
    def __init__(self) -> None:
        super().__init__()
        self.palavras_faceis = ['ROCHA', 'SOLO', 'FOSSIL']
        self.palavras_medias = ['CRATERA', 'MINERIO', 'PLACAS']
        self.palavras_dificeis = [
            'CLIMATOLOGIA', 'TEMPERATURA', 'UMIDADE', 'PRECIPITACAO', 'ESTRATOSFERA']

    def nivel_facil(self):
        # Embaralhando a ordem das palavras
        random.shuffle(self.palavras_faceis)
        pontos_no_nivel = 0

        for i, palavra in enumerate(self.palavras_faceis, start=1):
            system('cls')
            chances = 7
            print(f'Você tem {chances} chances')
            print(f'\n\nRodada {i}'.center(50))
            resultado = forca(palavra, chances, 250)
            pontos_no_nivel += resultado[1]

            if not resultado[0]:
                print(f'Jogo encerrado! Você jogou {i} rodadas')
                return False, pontos_no_nivel
            sleep(2)
        return True, pontos_no_nivel

    def nivel_medio(self):
        # Embaralhando a ordem das palavras
        random.shuffle(self.palavras_medias)
        pontos_no_nivel = 0

        for i, palavra in enumerate(self.palavras_medias, start=1):
            system('cls')
            chances = 7
            print(f'Você tem {chances} chances')
            print(f'\n\nRodada {i}'.center(50))
            resultado = forca(palavra, chances, 250)
            pontos_no_nivel += resultado[1]

            if not resultado[0]:
                print(f'Jogo encerrado! Você jogou {i} rodadas')
                return False, pontos_no_nivel
            sleep(2)
        return True, pontos_no_nivel

    def nivel_dificil(self):
        # Embaralhando a ordem das palavras
        random.shuffle(self.palavras_dificeis)
        pontos_no_nivel = 0

        for i, palavra in enumerate(self.palavras_dificeis, start=1):
            system('cls')
            chances = 7
            print(f'Você tem {chances} chances')
            print(f'\n\nRodada {i}'.center(50))
            resultado = forca(palavra, chances, 250)
            pontos_no_nivel += resultado[1]

            if not resultado[0]:
                print(f'Jogo encerrado! Você jogou {i} rodadas')
                return False, pontos_no_nivel
            sleep(2)
        return True, pontos_no_nivel


class Jogador:
    # Classe para instanciar o jogador e armazenar sua pontuação
    def __init__(self, nome) -> None:
        self.nome = nome if nome != '' else 'ANONIMO'
        self.__pontuacao = 0  # Atributo privado para evitar que o jogador tenha acesso

    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, valor):
        self.__pontuacao = valor

    def adicionar_pontuacao(self, valor):
        self.pontuacao += valor

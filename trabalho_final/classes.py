from abc import ABC, abstractclassmethod


# Classes que serão importadas para o arquivo main.py e será molde para os temas do jogo e instanciação do jogador

class Tema(ABC):
    # Classe Mãe de Geociências e Estatística: fornece a estrutura das classes filhas
    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def facil(self):
        ...

    @abstractclassmethod
    def medio(self):
        ...

    @abstractclassmethod
    def dificil(self):
        ...


class Estatistica(Tema):
    # Classe para as palavras relacionadas a Estatística
    def __init__(self) -> None:
        super().__init__()

    def facil(self):
        self.palavras_faceis = []
        return self.palavras_faceis

    def medio(self):
        self.palavras_medias = []
        return self.palavras_medias

    def dificil(self):
        self.palavras_dificeis = []
        return self.palavras_dificeis


class Geociencias(Tema):
    # Classe para as palavras relacionadas ao BCMT
    def __init__(self) -> None:
        super().__init__()
        self.palavras_faceis = []
        self.palavras_medias = []
        self.palavras_dificeis = []

    def facil(self):
        ...

    def medio(self):
        ...

    def dificil(self):
        ...


class Jogador:
    # Classe para instanciar o jogador e armazenar sua pontuação
    def __init__(self, nome='Anônimo') -> None:
        self.nome = nome
        self.__pontuacao = 0  # Atributo privado para evitar que burlem o sistema
        self.chances = 5

    @property
    def pontuacao(self):
        return self.__pontuacao

    @pontuacao.setter
    def pontuacao(self, valor):
        self.__pontuacao = valor

    def adicionar_pontuacao(self, valor):
        self.pontuacao += valor

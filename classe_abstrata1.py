'''
1) Uma biblioteca deseja criar um sistema de gerenciamento de seus itens. Os itens
disponíveis para empréstimo na biblioteca incluem livros, CDs e DVDs.
Cada item tem uma descrição específica:
- Livro: título e autor.
- CD: título e artista.
- DVD: título e diretor.

Você deve criar uma classe abstrata chamada ItemDescrição com os seguintes métodos:
- descrição(): um método abstrato que deve ser implementado em cada item específico (livro,
CD, DVD) para retornar sua descrição.
- emprestar(): um método que imprime a mensagem indicando que o item foi emprestado.
- devolver(): um método que imprime a mensagem indicando que o item foi devolvido.

Além disso, a biblioteca tem dois tipos de funcionários:
- Bibliotecário: Pode mostrar a descrição de um item e emprestar um item.
- Usuário: Pode devolver um item.
Ambos os Bibliotecário e Usuário têm um nome que deve ser usado nas interações, por
exemplo, ao emprestar ou devolver um item.

Tarefas:
Implemente a classe abstrata ItemDescrição.
Crie classes específicas para Livro, CD e DVD que herdem de ItemDescrição e
implementem o método descrição.
Implemente a classe Bibliotecário com um método para mostrar a descrição de um item e
outro para emprestar um item.
Implemente a classe Usuário com um método para devolver um item.
Crie testes para demonstrar a funcionalidade do seu sistema, instanciando os diferentes
itens e interagindo com as classes Bibliotecário e Usuário.

Dica: Utilize a funcionalidade from typing import Type para garantir que os métodos das
classes Bibliotecário e Usuário aceitem qualquer objeto que seja uma subclasse de
ItemDescrição.

DESAFIO: Quando um objeto for emprestado ou devolvido, o seu tipo deve ser apresentado
em letra minúscula. Ao invés de “O Livro A Arte da Guerra foi emprestado.”, deve ser “O
livro A Arte da Guerra foi emprestado.”

# Interface principal
livro = Livro("A Arte da Guerra", "Sun Tzu")
cd = CD("Thriller", "Michael Jackson")
dvd = DVD("O Poderoso Chefão", "Francis Ford Coppola")
bibliotecário = Bibliotecario("Martins")
usuario = Usuario("Pedro")bibliotecário.mostrar_descrição(livro)
bibliotecário.mostrar_descrição(cd)
bibliotecário.mostrar_descrição(dvd)
bibliotecário.emprestar_item(livro)
usuario.devolver_item(livro)
#Saída
Livro: A Arte da Guerra - Autor: Sun Tzu
CD: Thriller - Artista: Michael Jackson
DVD: O Poderoso Chefão - Diretor: Francis Ford Coppola
Martins está emprestando o item.
O Livro A Arte da Guerra foi emprestado.
Pedro está devolvendo o item.
O Livro A Arte da Guerra foi devolvido.'''

from abc import ABC, abstractmethod
from typing import Type


class ItemDescricao(ABC):
    def __init__(self, titulo, criador):
        self.titulo = titulo
        self.criador = criador

    @abstractmethod
    def descricao(self):
        if self.__class__ == Livro:
            print(f'Livro: {self.titulo} - Autor: {self.criador}')
        elif self.__class__ == CD:
            print(
                f'CD: {self.titulo} - Artista: {self.criador}')
        elif self.__class__ == DVD:
            print(
                f'DVD: {self.titulo} - Diretor: {self.criador}')

    @abstractmethod
    def emprestar(self):
        print(f'O {self.__class__.__name__.lower()} {self.titulo} foi emprestado.')

    @abstractmethod
    def devolver(self):
        print(f'O {self.__class__.__name__.lower()} {self.titulo} foi devolvido.')


class Livro(ItemDescricao):
    def __init__(self, titulo, criador):
        super().__init__(titulo, criador)

    def descricao(self):
        return super().descricao()

    def emprestar(self):
        return super().emprestar()

    def devolver(self):
        return super().devolver()


class CD(ItemDescricao):
    def __init__(self, titulo, criador):
        super().__init__(titulo, criador)

    def descricao(self):
        return super().descricao()

    def emprestar(self):
        return super().emprestar()

    def devolver(self):
        return super().devolver()


class DVD(ItemDescricao):
    def __init__(self, titulo, criador):
        super().__init__(titulo, criador)

    def descricao(self):
        return super().descricao()

    def emprestar(self):
        return super().emprestar()

    def devolver(self):
        return super().devolver()


class Bibliotecario:
    def __init__(self, nome):
        self.nome = nome

    def mostrar_descricao(self, item: Type[ItemDescricao]):
        item.descricao()

    def emprestar(self, item: Type[ItemDescricao]):
        print(f'{self.nome} está emprestando o item')
        item.emprestar()


class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def devolver(self, item: Type[ItemDescricao]):
        print(f'{self.nome} está devolvendo o item')
        item.devolver()


livro = Livro('Dom Casmurro', 'Machado de Assis')
cd = CD('Master of Puppets', 'Metallica')
dvd = DVD('The Dark Knight', 'Cristopher Nolan')

bibliotecario = Bibliotecario('Tatiana')
usuario = Usuario('Julia')

bibliotecario.mostrar_descricao(livro)
bibliotecario.mostrar_descricao(cd)
bibliotecario.mostrar_descricao(dvd)
print()
bibliotecario.emprestar(cd)
print()
usuario.devolver(cd)

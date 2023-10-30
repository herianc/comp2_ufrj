'''
Considere um sistema que trata de animais, e até o momento só contempla cachorros e
gatos. Todo animal deve emitir som, só que apenas cada tipo de animal é capaz de emitir
seu próprio som (cachorro faz au au e gato faz miau). Todo animal pode dormir e o sistema
indica que está dormindo, a saída inclui o nome do animal em questão. Todo animal
apresenta um método que indica sua fase de vida, só que apenas cada tipo de animal tem
sua própria divisão, isto é, na classe base ele serve como molde (vazio). O cachorro é
jovem até os 3 anos de idade, adulto entre 3 anos e 8 anos e depois disso é idoso. Para o
gato a mesma coisa, com os valores 4 e 10, depois disso é idoso. O método que indica a
fase da vida deve retornar a mensagem “<nome> tem <idade> anos e é [jovem, adulto ou
idoso]”.

Questionamento, se cachorro e gato usam nome e idade de animal, precisa de construtores
para eles?

Importante, o comando que emite a mensagem que indica a fase da vida deve ser
implementado uma única vez em um método só em uma classe só.

cachorro1 = Cachorro("Rex", 2)
print(cachorro1.emitir_som()) # Saída: Au Au
print(cachorro1.dormir()) # Saída: Rex está dormindo
print(cachorro1.fase_vida()) # Saída: Rex tem 2 anos e é jovem
gato1 = Gato("Whiskers", 6)
print(gato1.emitir_som()) # Saída: Miau
print(gato1.dormir()) # Saída: Whiskers está dormindo
print(gato1.fase_vida()) # Saída: Whiskers tem 6 anos e é adulto'''

from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def dormir(self):
        return f'{self.nome} está dormindo'

    @abstractmethod
    def emitir_som(self):
        if self.__class__ == Gato:
            return f'Miau'
        elif self.__class__ == Cachorro:
            return 'Au Au'

    @abstractmethod
    def fase_vida(self):
        ...


class Gato(Animal):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)

    def dormir(self):
        return super().dormir()

    def emitir_som(self):
        return super().emitir_som()

    def fase_vida(self):
        if self.idade < 4:
            return f'{self.nome} tem {self.idade} ano(s) e é jovem'
        elif self.idade >= 4 and self.idade <= 10:
            return f'{self.nome} tem {self.idade} ano(s) e é adulto'
        elif self.idade > 10:
            return f'{self.nome} tem {self.idade} ano(s) e é idoso'


class Cachorro(Animal):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)

    def dormir(self):
        return super().dormir()

    def emitir_som(self):
        return super().emitir_som()

    def fase_vida(self):
        if self.idade < 3:
            return f'{self.nome} tem {self.idade} ano(s) e é jovem'
        elif self.idade >= 3 and self.idade <= 8:
            return f'{self.nome} tem {self.idade} ano(s) e é adulto'
        elif self.idade > 8:
            return f'{self.nome} tem {self.idade} ano(s) e é idoso'


cachorro1 = Cachorro("Rex", 2)
print(cachorro1.emitir_som())  # Saída: Au Au
print(cachorro1.dormir())  # Saída: Rex está dormindo
print(cachorro1.fase_vida())  # Saída: Rex tem 2 anos e é jovem

gato1 = Gato("Whiskers", 6)
print(gato1.emitir_som())  # Saída: Miau
print(gato1.dormir())  # Saída: Whiskers está dormindo
print(gato1.fase_vida())  # Saída: Whiskers tem 6 anos e é adulto

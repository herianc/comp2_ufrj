""" Considere um ecossistema ecpecífico com animais diversos. 
Desevolva um código que tenha duas classes base: presa e predador. A presa está fugindo e 
o predador está caçando, estas são as suas ações principais.

Crie três classes geradoras de animais, uma delas cria animais que são presas, outra cria 
animais que são predadores e outra cria animais que são presa e predadores.
Quando se cria um animal oriundo da classe presa ele precisa fugir, um animal oriundo da classe 
predador precisa caçar, um animal que é presa e predador precisa tanto fugir como caçar.

A classe animal aqui não é um animal genérico abstrato, é uma classe geradora de animais de algum
tipo. Por exemplo: 'class Elefante'
"""


class Presa:
    def fugir(self):
        print(f'{self.__class__.__name__} está fugindo!')


class Predador:
    def cacar(self):
        print(f'{self.__class__.__name__} está caçando!')


class OncaPintada(Predador):
    pass


class Capivara(Presa):
    pass


class JacareDoPantanal(Presa, Predador):
    pass


onca = OncaPintada()
onca.cacar()

capivara = Capivara()
capivara.fugir()

jacare = JacareDoPantanal()
jacare.fugir()
jacare.cacar()

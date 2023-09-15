'''Exercício 2. Rinha de robôs (pode ser realizado com interação com o usuário ou não)

Imagine um cenário futurista onde robôs são programados para batalhar entre si em um
campeonato de máquinas.

Requisitos:
Classe Robô:

Cada robô possui os seguintes atributos:
    nome: Uma string representando o nome do robô. pontos_de_vida (PV): Um valor inteiro que inicia com um máximo de 50. Se um robô tentar
ser instanciado com mais de 50 PV, uma mensagem de erro deve ser exibida e o robô não deve ser criado.
    energia: Um valor inteiro que sempre começa em 100. 
    status: Uma string que pode ser "operante" ou "inoperante". Um robô inicia como "operante", mas se seus PV caírem para 0 ou menos, 
seu status deve mudar para "inoperante".

A classe Robô deve ter os seguintes métodos:

    - atacar(outro_robo, classe_de_ataque): Permite que um robô ataque outro robô. O dano do ataque é aleatório e depende da classe de ataque escolhida.
    - energizar(): Permite que um robô recupere energia.
    - recuperar(): Permite que um robô recupere PV à custa de energia.
    - implodir(outro_robo): Um robô pode se auto-destruir para causar dano ao oponente.

Ataque:
Os robôs podem atacar em três classes diferentes, que determinam a quantidade de dano e
energia consumida.Classe 1: Dano entre 1 e 8, consome 10 de energia.
Classe 2: Dano entre 2 e 12, consome 20 de energia.
Classe 3: Dano entre 4 e 24, consome 40 de energia.

Energizar e Recuperar:
energizar(): Recupera 20 de energia.
recuperar(): Gasta 10 de energia para recuperar 10 de PV. Os PVs não podem exceder o valor inicial do robô.

Implodir:
Um robô pode decidir se autodestruir com o método implodir(), causando dano a si mesmo igual a todos os seus PVs e causando um dano aleatório 
entre 10 a 50 ao oponente. Implodir gasta 40 de energia.


Tarefa:
Com base nos requisitos fornecidos, crie a classe Robo e instancie dois robôs, escolha o
nome de cada um. Em seguida, simule uma batalha entre eles usando os métodos
fornecidos até que um dos robôs se torne "inoperante". Ao final, anuncie o vencedor da
batalha.
Após cada método utilizado o sistema deve responder o máximo possível de informações
sobre os robôs para acompanhamento (PV atual, energia atual...)

'''



from random import randint


class Robo:
    def __init__(self, nome, pv) -> None:
        if pv > 50:
            print('O robô não pode ser criado.')
            return None
        else:
            self.nome = nome
            self.pv = pv
            self.energia = 100
        self.status = 'Operante' if self.pv > 0 else 'Inoperante'

    def atacar(self, outro_robo, classe_de_ataque):
        match classe_de_ataque:
            # classe 1 - dano 1 e 8 - consome 10 de energia
            case 1:
                dano = randint(1, 8)
                outro_robo.pv -= dano
                self.energia -= 10
                print(
                    f'\t⚔️  {self.nome} causou {dano} de dano em {outro_robo.nome}')
            # classe 2 - dano 2 e 12 - consome 20 de energia
            case 2:
                dano = randint(2, 12)
                outro_robo.pv -= dano
                self.energia -= 20
                print(
                    f'\t⚔️ ⚔️  {self.nome} causou {dano} de dano em {outro_robo.nome}')
            # classe 3 - dano 4 e 24 - consome 40 de energia
            case 3:
                dano = randint(4, 24)
                outro_robo.pv -= dano
                self.energia -= 40
                print(
                    f'\t⚔️ ⚔️ ⚔️  {self.nome} causou {dano} de dano em {outro_robo.nome}')
        if outro_robo.pv > 0:
            outro_robo.status = 'Inoperante'

    def energizar(self):
        self.energia += 20
        print(f'\t 💊  {self.nome} recuperou 20 de energia ')

    def recuperar(self):
        if self.pv <= 40:
            self.energia -= 10
            self.pv += 10
            print(f'\t❤️‍🩹  {self.nome} recuperou 10 PV')

    def implodir(self, outro_robo):
        if self.energia >= 40:
            dano = randint(10, 50)
            outro_robo.pv -= dano
            self.pv -= self.pv
            self.energia -= 40
            print(
                f'\t💣💣{self.nome} se suicidou-se causando {dano} de dano a {outro_robo.nome}')


robo1 = Robo('C3PO', 50)
robo2 = Robo('R2D2', 40)
turno = 1

print('RINHA DE ROBÔ 🤖🤖')
while robo1.pv > 0 and robo2.pv > 0:
    print(f'Turno: {turno}')

    if robo1.energia > 40:
        if robo1.pv < 10:
            robo1.implodir(robo2)
        elif robo1.pv < 15:
            robo1.recuperar()
        else:
            # A classe de ataque é aleatória
            robo1.atacar(robo2, randint(1, 3))
    else:
        robo1.energizar()

    if robo2.energia > 40:
        if robo2.pv < 10:
            robo2.implodir(robo1)
        elif robo2.pv < 15:
            robo2.recuperar()
        else:
            # A classe de ataque é aleatória
            robo2.atacar(robo1, randint(1, 3))
    else:
        robo2.energizar()

    if robo2.pv <= 0 and robo1.pv > 0:
        print('#'*50)
        print(f'{robo1.nome} é o GRANDE CAMPEÃO INTERGALÁTICO DA RINHA DE ROBOS 🎆🎆🎆🎆')
        print('#'*50)
        break
    elif robo1.pv <= 0 and robo1.pv > 0:
        print('#'*50)
        print(
            f'{robo2.nome} é o GRANDE CAMPEÃO INTERGALÁTICO DA RINHA DE ROBOS 🎆🎆🎆🎆')
        print('#'*50)
        break
    if robo1.pv <= 0 and robo2.pv <= 0:
        print('#'*50)
        print('Não acho que quem ganhar ou quem perder, nem quem ganhar nem perder, vai ganhar ou perder. Vai todo mundo perder.'.upper())
        print('EMPATE!')
        print('#'*50)
        break

    print(f'{robo1.nome} - 💓: {robo1.pv} - 🔵: {robo1.energia}')
    print(f'{robo2.nome} - 💓: {robo2.pv} - 🔵: {robo2.energia}')
    turno += 1
    input()

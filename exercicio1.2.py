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

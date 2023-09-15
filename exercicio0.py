'''Você foi contratado para modelar uma televisão em Python. A televisão possui as seguintes características e funcionalidades:

Características:

Polegadas (inteiro)
Marca (string)
Preço (float)
Estado (inicialmente desligada)
Canal (sempre começa em 1 quando a TV é ligada)
Volume (inicia em 1 da primeira vez e depois mantém o último valor definido pelo usuário, mesmo que a TV seja ligada ou desligada)
Funcionalidades:

Ligar e desligar a TV
Verificar se está ligada ou desligada
Mudar de canal (entre 1 e 4999)
Mudar o volume (entre 1 e 99). Se o volume for superior a 80, deve alertar o usuário sobre o som alto.
Mostrar todos os dados simultaneamente (canal, volume e marca). Se o volume estiver entre 81 e 99, indicar que o volume está alto.
Crie a classe Televisao para representar essas características e funcionalidades.'''


class Televisao():

    def __init__(self, polegadas, marca, preco, estado=False, canal=1, volume=1) -> None:
        self.polegadas = polegadas
        self.marca = marca
        self.preco = preco
        self.estado = estado
        self.canal = canal
        self.volume = volume
        self.canal = canal

    def Especificacoes(self):
        print(
            f'''Marca: {self.marca}\nPolegadas:{self.polegadas}\nCanal: {self.canal}\nVolume: {self.volume}\n''')
        if self.volume in range(81, 100):
            print('O volume está alto demais')

    def LigarDesligar(self):
        if not self.estado:
            self.estado = True
            print('ON\n')
        else:
            self.estado = False
            print('\nOFF')

    def Estado(self):
        print('TV Ligada' if self.estado else 'TV Desligada')

    def MudarCanal(self, novo_canal):
        if self.estado:
            self.canal = novo_canal
            print(f'Mudando canal\nCanal:{self.canal}')
        else:
            ...

    def MudarVolume(self, novo_volume):
        if self.estado:
            if novo_volume in range(1, 100):
                self.volume = novo_volume
                print(f'Mudando o volume\nVolume:{self.volume}')
                if self.volume > 80:
                    print('Volume muito alto!')
        else:
            print('TV Desligada! Não é possivel mudar o volume\n')


tv1 = Televisao(29, 'Samsung', 2000.00)

tv1.Especificacoes()
tv1.Estado()
tv1.LigarDesligar()
tv1.Estado()

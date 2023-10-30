"""
Considere um sistema de gerenciamento de veículos, com as seguintes com as seguintes classes:

Veículo: classe base que representa um veículo, com marca, modelo e ano.

Motorizado: classe que representa um veículo motorizado (que herda de veículos), com potência e 
combustível

Elétrico: classe que representa um veículo elétrico (que herda de veículo), com autonomia e tempo 
de recarga

Hibrido: classe que representa um veículo híbrido, que herda tanto de Motorizado quanto de Elétrico,
e possui capacidade do tanque de combustível e consumo médio de combustível.

Usando herança múltipla, a classe Híbrido deve ser capaz de acessar e modificar atributos de ambas 
as  classes mães. Além disso, devem implementar:

partir(): todo veículo deve ser capaz de iniciar o movimento. Deve indicar a marca e o modelo que 
está  em movimento.

alterar_combustivel(novo_combustivel): o carro motorizado pode alterar o combustivel do veiculo para 
o valor especificado. Antes da alteração, exiba uma mensagem informando o valor anterior e o novo 
valor do combustível

alterar_autonomia(nova_autonomia): o carro elétrico pode alterar a autonomia do veículo para o valor 
especificado. Antes da alteração, exiba uma mensagem informando o valor anterior e o novo valor da 
autonomia.

DESAFIO: faça esta questão com interação com o usuário. 

Deve ser capaz de instanciar motorizados, elétricos ou híbridos. 
"""


class Veiculo:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def partir(self):
        print(f'{self.marca} {self.modelo} {self.ano} está em movimento!')

    def detalhes(self):
        print(f'{self.marca} {self.modelo} {self.ano}')


class Motorizado(Veiculo):
    def __init__(self, marca, modelo, ano, potencia, combustivel) -> None:
        Veiculo.__init__(self, marca, modelo, ano)
        self.potencia = potencia
        self.combustivel = combustivel

    def alterar_combustivel(self, novo_combustivel):
        print(
            f'Alterando combustível de {self.combustivel} para {novo_combustivel}')
        self.combustivel = novo_combustivel


class Eletrico(Veiculo):
    def __init__(self, marca, modelo, ano, autonomia, tempo_recarga) -> None:
        Veiculo.__init__(self, marca, modelo, ano)
        self.autonomia = autonomia
        self.recarga = tempo_recarga

    def alterar_autonomia(self, nova_autonomia):
        print(f'Alterando autonomia de {self.autonomia} para {nova_autonomia}')
        self.autonomia = nova_autonomia


class Hibrido(Motorizado, Eletrico):
    def __init__(self, marca, modelo, ano, potencia, combustivel, autonomia, tempo_recarga, tanque, consumo) -> None:
        self.consumo = consumo
        self.tanque = tanque
        Motorizado.__init__(self, marca, modelo, ano, potencia, combustivel)
        Eletrico.__init__(self, marca, modelo, ano, autonomia, tempo_recarga)


carro1 = Motorizado('Chevrolet', 'Onix LT', 2022, '100cv', 'Gasolina')
carro1.alterar_combustivel('Etanol')
carro1.partir()
print()
carro2 = Eletrico('Tesla', 'Model 3', 2020, 500, 30)
carro2.alterar_autonomia(600)
carro2.partir()
print()
carro3 = Hibrido('Toyota', 'Model 3', 2019, '100hp',
                 'Gasolina', 200, 25, 40, 15)
carro3.partir()
carro3.alterar_combustivel('Etanol')
carro3.alterar_autonomia(220)
print()


veiculos_motorizados = []
veiculos_eletricos = []
veiculos_hibridos = []

# DESAFIO: INTERAÇÃO COM O USUÁRIO
while True:

    escolha = int(input(
        '\nCrie o seu carro:\n1 - Motorizado\n2 - Eletrico\n3 - Hibrido\n4 - Listar Veículos\n0 - Sair\n'))

    match escolha:
        case 1:
            marca = input('Marca do veículo: ')
            modelo = input('Modelo: ')
            ano = int(input('Ano do modelo: '))
            potencia = input('Potência do motor: ')
            combustivel = input('Combustível do veículo: ')

            carro_motorizado = Motorizado(
                marca, modelo, ano, potencia, combustivel)
            veiculos_motorizados.append(carro_motorizado)

        case 2:
            marca = input('Marca do veículo: ')
            modelo = input('Modelo: ')
            ano = int(input('Ano do modelo: '))
            autonomia = int(input('Autonomia do veículo: '))
            tempo_recarga = int(input('O tempo de recarga da bateria: '))

            carro_eletrico = Eletrico(
                marca, modelo, ano, autonomia, tempo_recarga)
            veiculos_eletricos.append(carro_eletrico)

        case 3:
            marca = input('Marca do veículo: ')
            modelo = input('Modelo: ')
            ano = int(input('Ano do modelo: '))
            potencia = input('Potência do motor: ')
            combustivel = input('Combustível do veículo: ')
            autonomia = int(input('Autonomia do veículo: '))
            tempo_recarga = int(input('O tempo de recarga da bateria: '))
            tanque = int(input('Capacidade do tanque de combustível: '))
            consumo = int(input('Consumo médio do veículo: '))

            carro_hibrido = Hibrido(marca, modelo, ano, potencia,
                                    combustivel, autonomia, tempo_recarga, tanque, consumo)
            veiculos_hibridos.append(carro_hibrido)

        case 4:
            print('\nVEICULOS MOTORIZADOS:')
            for veiculo in veiculos_motorizados:
                print(f'{veiculo.marca} {veiculo.modelo} {veiculo.ano}')

            print('\nVEICULOS ELÉTRICOS:')
            for veiculo in veiculos_eletricos:
                print(f'{veiculo.marca} {veiculo.modelo} {veiculo.ano}')

            print('\nVEICULOS HÍBRIDOS:')
            for veiculo in veiculos_hibridos:
                print(f'{veiculo.marca} {veiculo.modelo} {veiculo.ano}')

        case 0:
            print('Encerrando...')
            break

        case _:
            print('Inválido!')

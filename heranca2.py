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
        print(f'{self.marca} {self.modelo} está em movimento!')


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


carro_motorizado = Motorizado(
    'Chevrolet', 'Onix LT', 2022, '100cv', 'Gasolina')
carro_motorizado.partir()
carro_motorizado.alterar_combustivel('Etanol')


carro_eletrico = Eletrico('Tesla', 'Model 3', 2020, 500, 30)
carro_eletrico.alterar_autonomia(600)
carro_eletrico.partir()

carro3 = Hibrido('Toyota', 'Prius', 2022, '100hp', 'Gasolina', 500, 45, 40, 20)
carro3.partir()
carro3.alterar_autonomia(600)

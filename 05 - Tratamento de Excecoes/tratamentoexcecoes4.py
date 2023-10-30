class AluguelException(Exception):
    def __init__(self, mensagem) -> None:
        super().__init__(mensagem)
        self.mensagem = mensagem


class Veiculo:
    def __init__(self, placa: str, modelo: str) -> None:
        self.placa = placa
        self.modelo = modelo
        self.disponivel = True

    def alugar(self):
        if self.disponivel:
            self.disponivel = False
            print(f'Veiculo: {self.modelo} - Placa: {self.placa} foi alugado.')
        else:
            raise AluguelException('Veículo não disponível para aluguel')

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f'Veiculo: {self.modelo} - Placa: {self.placa} devolvido.')
        else:
            raise AluguelException('Veículo já está disponível')

    def __str__(self):
        return f'Veiculo: {self.modelo} - Placa: {self.placa} - Disponível: {self.disponivel}.'


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.veiculos_alugados = []

    def alugar_veiculo(self, veiculo):
        if len(self.veiculos_alugados) < 2 and veiculo.disponivel:
            self.veiculos_alugados.append(veiculo)
            veiculo.alugar()
            print(f'{self.nome} alugou o {veiculo.modelo}')
        else:
            raise AluguelException(
                'Carro não disponível ou limite de aluguéis excedido')

    def devolver_veiculo(self, veiculo):
        if veiculo in self.veiculos_alugados:
            self.veiculos_alugados.remove(veiculo)
            veiculo.devolver()
            print(f'{self.nome} devolveu o {veiculo.modelo}')
        else:
            raise AluguelException(
                'Veículo ainda não foi alugado.Não é possivel devolve-lo')

    def __str__(self) -> str:
        return f"Cliente: {self.nome} - Veículos alugados: {len(self.veiculos_alugados)}:"


class Garagem:
    def __init__(self) -> None:
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def listar_veiculos(self):
        for veiculo in self.veiculos:
            print(veiculo)

    def __str__(self) -> str:
        return f'Garagem: {len(self.veiculos)} veículos disponíveis".'


toyota = Veiculo('VAS777', 'Toyota Supra')
golf = Veiculo('FLA123', 'Golf Gti')
palio = Veiculo('FLU3C', 'Fiat Palio')

garagem = Garagem()
garagem.adicionar_veiculo(toyota)
garagem.adicionar_veiculo(golf)
garagem.adicionar_veiculo(palio)
garagem.listar_veiculos()
print(garagem)

cliente1 = Cliente('Jorgin Marreta')
cliente1.alugar_veiculo(toyota)
cliente1.alugar_veiculo(palio)
print(cliente1)

cliente2 = Cliente('Vagner Biceps')
cliente2.alugar_veiculo(golf)

class TransacaoBancariaException(Exception):
    def __init__(self, mensagem) -> None:
        super().__init__(mensagem)


class ContaBancaria:
    def __init__(self, saldo: float, titular) -> None:
        if saldo < 0:
            raise TransacaoBancariaException(
                'Saldo inicial não pode ser negativo.')
        self.saldo = saldo
        self.titular = titular

    def __str__(self) -> str:
        print(f'Conta de {self.titular} - Saldo: R$ {self.saldo:.2f}')


class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo: float, titular, taxa_juros) -> None:
        super().__init__(saldo, titular)
        self.juros = taxa_juros

    def calcular_juros(self, meses):
        try:
            if meses < 0:
                raise TransacaoBancariaException(
                    'Número de meses deve ser não negativo!')

            else:
                projecao = self.saldo + self.saldo * (self.juros/100) * meses
                print(
                    f'Daqui a {meses} meses o seu saldo será de R${projecao}')

        finally:
            self.__str__()
            print('Transação concluída!')

    def saque(self, valor):
        try:
            if valor > self.saldo:
                raise TransacaoBancariaException(
                    'Saldo insuficiente para a retirada!')
            elif valor < 0:
                raise TransacaoBancariaException('Valor de saque inválido!')
            else:
                self.saldo -= valor
                print(
                    f'Valor retirado: R${valor:.2f} - Saldo atual: R${self.saldo:.2f}')
        finally:
            print('Transação Concluída!')
            self.__str__()

    def __str__(self) -> str:
        print(
            f'Conta Poupança de {self.titular} - Saldo: R$ {self.saldo:.2f} - Taxa de Juros: {self.juros}%\n')


conta1 = ContaBancaria(500.00, 'José')

conta2 = ContaPoupanca(500.00, 'Ana', 1.5)
conta2.calcular_juros(12)
conta2.saque(40)

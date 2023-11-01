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
                self.__str__()
                projecao = self.saldo + self.saldo * (self.juros/100) * meses
                print(
                    f'Daqui a {meses} meses o seu saldo será de R${projecao}')
        except ValueError:
            raise TransacaoBancariaException(
                'Entrada para meses inválida! Digite apenas números')
        except:
            raise TransacaoBancariaException('Erro inesperado!')
        finally:
            print('Transação concluída!\n')

    def saque(self, valor):
        try:
            if valor > self.saldo:
                raise TransacaoBancariaException(
                    'Saldo insuficiente para a retirada!')
            elif valor < 0:
                raise TransacaoBancariaException('Valor de saque inválido!')
            else:
                self.__str__()
                self.saldo -= valor
                print(
                    f'Valor retirado: R${valor:.2f} - Saldo atual: R${self.saldo:.2f}')
        except ValueError:
            raise TransacaoBancariaException(
                'Entrada inválida! Digite apenas números.')
        except:
            raise TransacaoBancariaException('Erro inesperado!')
        finally:
            print('Transação Concluída!\n')

    def deposito(self, valor):
        try:
            if valor <= 0:
                raise TransacaoBancariaException('Valor de depósito inválido!')
            else:
                self.__str__()
                self.saldo += valor
                print(
                    f'Valor depositado: R${valor:.2f} - Saldo: R${self.saldo:.2f}')
        except ValueError:
            raise TransacaoBancariaException(
                'Entrada inválida! Digite apenas números.')
        finally:
            print('Transação concluída!')

    def __str__(self) -> str:
        print(
            f'Conta Poupança de {self.titular} - Saldo: R$ {self.saldo:.2f} - Taxa de Juros: {self.juros}%')


conta1 = ContaBancaria(500.00, 'José')

conta2 = ContaPoupanca(500.00, 'Ana', 1.5)
conta2.calcular_juros(12)
conta2.saque(40)

"""2) Você foi contratado por uma startup de tecnologia financeira para desenvolver um módulo de
gerenciamento de contas bancárias em Python. O principal objetivo é criar um sistema que seja
robusto e resiliente a erros comuns de entrada e operação.
O sistema é um menu interativo simples que permite ao usuário realizar operações básicas de
uma conta bancária, como depositar dinheiro, sacar dinheiro e verificar o saldo.

**Modelo de Conta Bancária**:
* Cada conta deve ter um saldo inicial ao ser criada.
* Deve ser possível depositar dinheiro na conta.
* Deve ser possível sacar dinheiro da conta.
* Deve ser possível consultar o saldo atual da conta.

**Tratamento de Exceções**:
* O sistema não deve permitir saques que ultrapassem o saldo atual da conta. Se o usuário
tentar sacar um valor maior do que o disponível, o sistema deve exibir uma mensagem de erro
informando que o saldo é insuficiente.
* O sistema não deve aceitar valores de depósito ou saque que sejam negativos ou zero. Se
tal entrada for detectada, o sistema deve informar ao usuário que o valor inserido é inválido.
* Se o usuário inserir uma entrada não numérica ao tentar depositar ou sacar dinheiro, o
sistema deve informar ao usuário sobre o erro e pedir que ele insira um valor válido.

**Interface do Usuário**:
* O programa deve exibir um menu com as opções disponíveis: depositar, sacar, verificar
saldo e sair.
* A cada operação realizada (saque ou depósito), o sistema deve confirmar a operação ao
usuário, exibindo uma mensagem apropriada.
* Ao escolher consultar o saldo, o sistema deve exibir o saldo atual da conta.
* O sistema deve permitir que o usuário faça várias operações sem precisar reiniciar o
programa e deve continuar rodando até que o usuário decida sair.
"""

saldo = 0

while True:
    print('\n\nBanco Pythonico'.center(40).upper())
    operacao = input(
        '1 - Depósito\n2 - Saque\n3 - Verificar saldo da conta\n4 - Encerrar operação\n')

    match operacao:
        case '1':
            try:
                deposito = float(input('Valor do depósito: R$'))
                if deposito <= 0:
                    print('Valor de depósito inválido.'.upper())
                    continue
                else:
                    saldo += deposito
                    print(
                        f'\nR$ {deposito:.2f} depositado em sua conta.\nSaldo atual: R${saldo:.2f}')
            except ValueError:
                print('Entrada inválida! Digite apenas valores numericos'.upper())

        case '2':
            try:
                saque = float(input('Valor do saque: R$'))
                if saque <= 0:
                    print('Valor de saque inválido.'.upper())
                    continue
                if saque > saldo:
                    print(
                        f'Saldo insuficiente para saque.\nSaldo:{saldo}'.upper())
                    continue
                else:
                    saldo -= saque
                    print(
                        f'\nR$ {saque:.2f} retirado de sua conta.\nSaldo atual: R${saldo:.2f}')
            except ValueError:
                print('Entrada inválida! Digite apenas números')

        case '3':
            print(f'\nSaldo atual da conta: R$ {saldo:.2f}')
        case '4':
            print('Encerrando...')
            break
        case _:  # Esta linha trata as excecões das entradas do menu
            print('Entrada inválida! Digite uma das opções.'.upper())

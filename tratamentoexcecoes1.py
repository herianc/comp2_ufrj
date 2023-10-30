"""
1) Você foi contratado para desenvolver um sistema simples que faz a divisão de dois números.
O sistema deve solicitar ao usuário dois números e realizar a divisão do primeiro pelo segundo.
Porém, sabendo que divisões por zero são inválidas e que os usuários podem digitar valores
não numéricos, é seu trabalho garantir que o programa funcione sem erros em todos os
cenários possíveis.

- O programa deve solicitar ao usuário dois números.
- Deve ser feita a divisão do primeiro número pelo segundo.
- Caso o usuário digite um valor não numérico, o sistema deve informá-lo de que o valor
inserido não é um número e pedir para tentar novamente.
- Se o segundo número for zero, o programa deve alertar o usuário que divisão por zero é
inválida e solicitar um novo valor.
- Se a divisão ocorrer sem problemas, o programa deve exibir o resultado.

O programa deve rodar indefinidamente até que haja um resultado válido, sem erro.
Ao executar o programa, ele solicitará ao usuário que insira dois números. Se o usuário inserir
algo que não seja um número, será exibida uma mensagem informando que o valor inserido
não é um número. Se o segundo número for zero, o programa informará que a divisão por zero
é inválida. Caso contrário, o programa exibirá o resultado da divisão e terminará."""

while True:
    try:
        dividendo = int(input('Dividendo (Valor a ser dividido):  '))
        divisor = int(input('Divisor: '))
        print('\nResultado: ', dividendo/divisor)
        break

    except ValueError:
        print('\nEntrada inválida! Digite apenas números\n'.upper())
        continue

    except ZeroDivisionError:
        print('\nO divisor deve ser diferente de zero\n'.upper())
        continue

    except:
        print('Erro inesperado!')
        continue

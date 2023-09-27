'''Você foi contratado por uma startup de entretenimento para desenvolver um sistema
simples de gerenciamento de mídias. As mídias podem ser tanto músicas (canções) quanto
podcasts. Cada mídia possui um título, duração e autor. Canção e Podcast são mídias.

Classe Midia:
Deve ter um construtor que receba o título, duração e autor.
Deve possuir um método play() que exibe uma mensagem indicando que a mídia está
sendo reproduzida.
Deve possuir um método informacoes() que retorna informações básicas sobre a mídia:
título, autor e duração.

Classe Cancao:
Além das propriedades de uma mídia, uma canção possui um gênero musical.
O método informacoes() deve ser sobrescrito para incluir o gênero da canção. Neste
método deve ser indicado que é uma canção (adicional, de maneira automática)

Classe Podcast:
Além das propriedades de uma mídia, um podcast tem um tema principal.
O método informacoes() deve ser sobrescrito para incluir o tema do podcast. Neste método
deve ser indicado que é um podcast (adicional, de maneira automática)

Atributo Autor:
O atributo autor deve ser privado e somente ele deve possuir métodos de acesso (getters e
setters) usando os decoradores de Python.

Aplicativo Principal:
O aplicativo principal deve oferecer um menu para o usuário, permitindo adicionar canções
ou podcasts, listar e reproduzir as mídias adicionadas e sair do programa.
Desenvolva este sistema de gerenciamento de mídias, atendendo aos requisitos acima
OBS.: Caso tenha problemas gerando os objetos, crie a main como uma função. Após
desenvolver as classes insira:
def main():
[aqui segue o código da interface principal]
if __name__ == "__main__":
main()
Sugestão de código principal e respectiva saída (em azul):
Gerenciador de Mídias
1. Adicionar canção
2. Adicionar podcast
3. Listar e reproduzir mídias
4. Sair
Escolha uma opção:'''


class Midia:
    def __init__(self, titulo, duracao, autor) -> None:
        self.titulo = titulo
        self.duracao = duracao
        self.__autor = autor

    def play(self):
        print(f'Reproduzindo {self.titulo}...')

    def informacoes(self):
        print(
            f'Título: {self.titulo}, Autor: {self.__autor}, Duração: {self.duracao}')

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, novo_autor):
        self.__autor = novo_autor


class Cancao(Midia):
    def __init__(self, titulo, duracao, autor, genero) -> None:
        super().__init__(titulo, duracao, autor)
        self.genero = genero

    def informacoes(self):
        print(
            f'Canção - Título: {self.titulo} - {self.autor} - {self.duracao}\
 - {self.genero}')


class Podcast(Midia):
    def __init__(self, titulo, duracao, autor, tema) -> None:
        super().__init__(titulo, duracao, autor)
        self.tema = tema

    def informacoes(self):
        print(
            f'Podcast - Título: {self.titulo} - {self.autor} - {self.duracao}\
 - {self.tema}')


# Instanciando e armazenando os objetos
midias = []

msg = '''
Gerenciador de Mídias
1. Adicionar canção
2. Adicionar podcast
3. Listar e reproduzir mídias
4. Sair
Escolha uma opção:'''

while True:
    escolha = int(input(msg))

    match escolha:
        case 1:
            print()
            titulo = input('Título: ')
            duracao = input('Duração: ')
            autor = input('Autor: ')
            genero = input('Genero: ')

            cancao = Cancao(titulo, duracao, autor, genero)
            midias.append(cancao)

        case 2:
            print()
            titulo = input('Título: ')
            duracao = input('Duração: ')
            autor = input('Autor: ')
            tema = input('Tema: ')

            podcast = Podcast(titulo, duracao, autor, tema)
            midias.append(podcast)

        case 3:
            print()
            for midia in midias:
                print('-'*50)
                midia.informacoes()
                midia.play()
                print('-'*50)

        case 4:
            print('Encerrando...')
            break

        case _:
            print('\nDigite uma escolha válida\n')

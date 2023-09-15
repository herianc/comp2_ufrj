'''
Exercício 1. Sistema de Gerenciamento de Biblioteca
Você foi contratado para desenvolver um sistema simples de gerenciamento para uma
biblioteca. O objetivo principal é acompanhar quais livros estão disponíveis, quais estão
emprestados e a capacidade de emprestar e retornar livros. Deve apresentar:

1. Classe Livro:
Cada livro tem os seguintes atributos:
- `titulo`: Uma string representando o título do livro.
- `autor`: Uma string representando o autor do livro.
- `status`: Uma string que pode ser "disponível" ou "emprestado".

A classe Livro deve ter os seguintes métodos:
- `emprestar()`: Altera o status do livro para "emprestado".
- `retornar()`: Altera o status do livro para "disponível".

2. Classe Biblioteca:
A biblioteca tem o seguinte atributo:
- `livros`: Uma lista contendo todos os livros disponíveis na biblioteca.

A classe Biblioteca deve ter os seguintes métodos:
- `adicionar_livro(livro)`: Adiciona um livro à lista de livros.
- `listar_livros()`: Exibe todos os livros e seus respectivos status.
- `emprestar_livro(titulo)`: Procura um livro pelo título e, se disponível, o empresta.
- `retornar_livro(titulo)`: Procura um livro pelo título e o retorna, se estiver emprestado.

Tarefa:
Crie as classes `Livro` e `Biblioteca` e implemente seus métodos. Depois, crie uma interface
simples para o usuário, onde ele pode adicionar livros à biblioteca, listar todos os livros,
emprestar e retornar livros.
Mesmo que não seja ideal, a resolução é simples e a biblioteca tem apenas um exemplar de
cada título'''


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = 'Disponível'

    def emprestar(self):
        if self.status == 'Disponível':
            self.status = 'Emprestado'
        else:
            print('O livro está emprestado')

    def retornar(self):
        if self.status == 'Emprestado':
            self.status = 'Disponível'
        else:
            print('O livro já está disponível')


class Biblioteca():
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor):
        self.livros.append(Livro(titulo, autor))

    def listar_livros(self):
        print('-'*5, 'LISTAGEM DE LIVROS DA BIBLIOTECA', '-'*5)
        for i, livro in enumerate(self.livros):
            print(
                f'{i+1} - {livro.titulo}, {livro.autor}  -  Status: {livro.status.upper()}')

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.emprestar()

    def retornar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.retornar()


biblioteca = Biblioteca()


print('-'*6, 'SISTEMA DE GERENCIAMENTO DA BIBLIOTECA DA UFRJ', '-'*6)
print('''
      1 - Adicionar livro
      2 - Listar os livros da biblioteca
      3 - Pegar um titulo emprestado
      4 - Retornar um livro''')
while True:
    escolha = int(input('\nDigite sua escolha (0 - Sair): '))

    match escolha:
        case 0:
            print('Encerrando...')
            break
        case 1:
            titulo = input('Titulo: ')
            autor = input('Autor: ')
            biblioteca.adicionar_livro(titulo, autor)
        case 2:
            biblioteca.listar_livros()
        case 3:
            titulo = input('Titulo: ')
            biblioteca.emprestar_livro(titulo)
            print(f'')
        case 4:
            titulo = input('Titulo: ')
            biblioteca.retornar_livro(titulo)
        case _:
            print('Escolha inválida')

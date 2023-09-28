"""Sistema de Gestão de Produtos em uma Loja

Imagine que você está desenvolvendo um sistema para gerenciar produtos em uma loja. A loja vende 
diversos produtos, como Livros, Eletrônicos e Roupas. Cada tipo de produto tem especificidades e ações diferentes.

Especificações:

Classe Produto:
Atributos:
nome: Nome do produto.
preco: Preço do produto.
Métodos:
desconto(): Retorna o preço com um desconto básico de 5%.
detalhes(): Retorna uma string com o nome e o preço do produto.

Classe Livro:
Deve herdar de Produto.
Atributos adicionais:
autor: Autor do livro.
paginas: Número de páginas do livro.
Métodos:
desconto(): Retorna o preço com um desconto de 10%.
detalhes(): Além das informações do produto (sobrescrita do método), exibe o autor e o número de páginas.

Classe Eletronico:
Deve herdar de Produto.
Atributos adicionais:
marca: Marca do produto eletrônico.
Métodos:
desconto(): Retorna o preço com um desconto de 8%.
detalhes(): Além das informações do produto (sobrescrita do método), exibe a marca (override).

Classe Roupa:
Deve herdar de Produto.
Atributos adicionais:
tamanho: Tamanho da roupa (P, M, G).
Métodos:
desconto(): Retorna o preço com um desconto de 5%.
detalhes(): Além das informações do produto (sobrescrita do método), exibe o tamanho.

Seu sistema deve ser capaz de gerenciar uma lista de produtos, identificar seu tipo, aplicar descontos 
e exibir detalhes específicos de cada produto através do polimorfismo."""


class Produto:
    def __init__(self, nome: str, preco: int):
        self.preco = preco
        self.nome = nome

    def desconto(self):
        desconto = self.preco * 0.05
        self.preco -= desconto

    def detalhes(self):
        print(f'Nome: {self.nome}, Preço: R${self.preco}')


class Livro(Produto):
    def __init__(self, nome, preco: int, autor, paginas):
        super().__init__(nome, preco)
        self.autor = autor
        self.paginas = paginas

    def desconto(self):
        desconto = self.preco * 0.1
        self.preco -= desconto

    def detalhes(self):
        print(
            f'Nome: {self.nome}, Preço: R${self.preco}\nAutor: {self.autor}, Nº páginas: {self.paginas}')


class Eletronico(Produto):
    def __init__(self, nome, preco: int, marca):
        super().__init__(nome, preco)
        self.marca = marca

    def desconto(self):
        desconto = self.preco * 0.08
        self.preco -= desconto

    def detalhes(self):
        print(
            f'Nome: {self.nome}, Preço: R${self.preco}, Marca: {self.marca}')


class Roupa(Produto):
    def __init__(self, nome, preco: int, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    def desconto(self):
        desconto = self.preco * 0.05
        self.preco -= desconto

    def detalhes(self):
        print(
            f'Nome: {self.nome}, Preço: R${self.preco}, Marca: {self.tamanho}')


cadeira = Produto('Cadeira', 45)
cadeira.detalhes()
cadeira.desconto()
cadeira.detalhes()
print()

livro = Livro('Dom Casmurro', 20, 'Machado de Assis', '208')
livro.detalhes()
livro.desconto()
livro.detalhes()
print()

camisa_vasco = Roupa('Camisa do Vascão', 220, 'M')
camisa_vasco.detalhes()
camisa_vasco.desconto()
camisa_vasco.detalhes()

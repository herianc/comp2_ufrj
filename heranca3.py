"""
Sistema de Gestão de Produtos

Imagine que estamos desenvolvendo um sistem para gerenciar diferentes
tipos de produtos em uma loja. Temos três categorias principais: produtos em geral,
produtos eletrônicos e smartphones. Cada categoria tem suas características e especificades.
Um smartphone é um eletrônico, e um eletrônico é um produto, que é a abstração mais alta.

Requisitos:

Classe Produto:
Atributos 
nome: Nome do produto
preco: Preço do produto

Métodos
exibir_detalhes(): Mostra os detalhes básicos do produto.


Classe Eletronico:
Atributos adicionais
garantia: Anos de garantia do porduto eletrônico.
marca: Marca do produto.

Métodos adicionais
mostrar_garantia(): Exibe a duração da garantia do produto.


Classe Smartphone:
Atributos adicionais 
sistema_operacional: Sistema operacional do smartphone
capacidade_armazenamento: Capacidade de armazenamento em GB

Métodos adicionais
exibir_especificacoes(): Mostra as especificações completas do smartphone. 

Crie as classes Produto, Eletronico e Smartphone e implemente seus métodos conforme descrito.
Em seguida, crie instâncias destas classes para simular produtos sendo adicionados ao sistema 
e exibindo suas informações.

"""


class Produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

    def exibir_detalhes(self):
        print(f'Nome: {self.nome} - Preço: $ {self.preco}')


class Eletronico(Produto):
    def __init__(self, nome, preco, garantia, marca) -> None:
        self.garantia = garantia
        self.marca = marca
        super().__init__(nome, preco)

    def mostrar_garantia(self):
        print(f'{self.nome} tem {self.garantia} anos de garantia')


class Smartphone(Eletronico):
    def __init__(self, nome, preco, garantia, marca, so, armazenamento) -> None:
        self.so = so
        self.armazenamento = armazenamento
        super().__init__(nome, preco, garantia, marca)

    def exibir_especificacoes(self):
        print(
            f'Produto: {self.nome}, Preço: {self.preco}, Marca: {self.marca}, Garantia: {self.garantia}')
        print(
            f'Sistema Operancional: {self.so}, Armazenamento: {self.armazenamento}GB')


cadeira = Produto('Cadeira', 50)
cadeira.exibir_detalhes()

notebook = Eletronico('Notebook', 2500, 1, 'Samsung')
notebook.exibir_detalhes()
notebook.mostrar_garantia()

espertofone = Smartphone('Mi Note 11', 1400, 0, 'Xiaomi', 'Android', 128)
espertofone.exibir_especificacoes()

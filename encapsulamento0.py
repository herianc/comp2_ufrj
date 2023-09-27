'''Sistema de Gestão de Produtos. Desenvolva um sistema para gerenciar produtos em uma loja:

Classe Produto:
Atributos privados:
__preco: Preço do produto.
__descricao: Descrição do produto.

Métodos:
get_info(): Retorna uma string no formato "Descrição do produto: Preço".

Classe ProdutoImportado:
Deve herdar da classe Produto.
Atributos adicionais privados:
__taxa_importacao: Taxa de importação em porcentagem.
Métodos:
get_info(): Sobrescreve o método da classe pai e retorna "Descrição
do produto (Importado): Preço (com taxas)".
Implemente o encapsulamento utilizando propriedades, garantindo que
os atributos privados das classes sejam acessados e modificados
apenas através de métodos e não diretamente.

'''


class Produto:
    def __init__(self, preco, descricao):
        self.__preco = preco
        self.__descricao = descricao

    def __get_info(self):
        return f'Descrição do produto: {self.__preco}'

    @property  # Getter
    def preco(self):
        return self.__preco

    @preco.setter  # Setter
    def preco(self, novo_valor):
        self.__preco = novo_valor

    @property
    def descricao(self):
        return self.__descricao


class ProdutoImportado(Produto):
    def __init__(self, preco: int, descricao: str, taxa_importacao: int):
        self.__taxa_importacao = taxa_importacao / 100
        super().__init__(preco, descricao)

    def get_info(self):
        return f'Descrição do produto (Importado): \
Preço: {self.preco + self.preco * self.__taxa_importacao}'


miband = ProdutoImportado(250, 'Smartband', 17)
print(miband.get_info())

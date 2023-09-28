'''Você é um desenvolvedor em uma empresa de comércio eletrônico. Sua missão é
desenvolver um sistema simples que gerencia produtos. Além dos produtos normais, sua
empresa vende produtos importados, e você deve ser capaz de calcular o preço desses
produtos incluindo uma taxa de importação.

Classe Produto:
Deve possuir um atributo privado, preco e um público, descricao.
Implemente os métodos getters e setters usando os decoradores.
Implemente um método get_info que retorna uma string no formato "<a descrição do
produto>: <o preço do produto>".

Classe ProdutoImportado:
Produtos importados são produtos.
Deve possuir um atributo taxa_importacao, que representa a porcentagem da taxa de
importação.
Ao instanciar um ProdutoImportado, o preço final do produto deve ser atualizado
considerando a taxa de importação. Por exemplo, um produto de R$ 100,00 com uma taxa
de importação de 20% deve ter seu preço final ajustado para R$ 120,00.
O método get_info deve ser sobrescrito para incluir a palavra "(Importado)" após a
descrição do produto.

Instruções adicionais:
Após implementar as classes, crie uma instância da classe Produto e outra da classe
ProdutoImportado. Utilize o método get_info para exibir as informações dos produtos e
verifique se os preços estão sendo calculados corretamente para os produtos importados.'''


class Produto:
    def __init__(self, preco: int, descricao: str) -> None:
        self.__preco = preco
        self.descricao = descricao

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco

    def get_info(self):
        return f'{self.descricao}: R${self.preco}'


class ProdutoImportado(Produto):
    def __init__(self, preco: int, descricao: str, taxa_importacao: int) -> None:
        super().__init__(preco, descricao)
        self.taxa_importacao = taxa_importacao / 100
        self.preco = self.preco + self.preco * self.taxa_importacao

    def get_info(self):
        return f'{self.descricao} (Importado): R${self.preco:.2f}'


camisa_vasco = Produto(250, 'Camisa do Gigante')
print(camisa_vasco.get_info())

miband = ProdutoImportado(220, 'Xiaomi Mi Band', 10)
print(miband.get_info())

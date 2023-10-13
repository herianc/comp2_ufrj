from abc import ABC, abstractmethod


class ProdutosGerais(ABC):
    def __init__(self, codigo, nome, preco) -> None:
        self.codigo = codigo.upper()
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def informacoes_basicas(self):
        ...


class Eletronico(ProdutosGerais):
    def __init__(self, codigo, nome, preco, voltagem) -> None:
        self.voltagem = voltagem
        super().__init__(codigo, nome, preco)

    def informacoes_basicas(self):
        return f'Eletronico: {self.nome} - Voltagem: {self.voltagem}'


class Alimento(ProdutosGerais):
    def __init__(self, codigo, nome, preco, validade) -> None:
        super().__init__(codigo, nome, preco)
        self.validade = validade

    def informacoes_basicas(self):
        return f'Alimento: {self.nome} - Data de Validade: {self.validade}'


class Estoque:
    def __init__(self) -> None:
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.informacoes_basicas())

    def buscar_produto(self, codigo):
        print(f'Buscando produto pelo código {codigo}')
        msg = None
        for produto in self.produtos:
            if codigo == produto.codigo:
                msg = f'Produto encontrado:', produto.informacoes_basicas()
                break

        # if ternário para saber se a msg foi subscrita
        print(*msg) if msg else print('Produto não encontrado.')


estoque = Estoque()
estoque.adicionar_produto(Eletronico(
    'W762', 'Monitor Philips 29"', 999.00, '220v'))
estoque.adicionar_produto(
    Alimento('B689', 'Coca-Cola Lata', 3.99, "28/10/2023"))
estoque.listar_produtos()

print()
estoque.buscar_produto("W762")
print()
estoque.buscar_produto("A789")
print()
estoque.buscar_produto("B689")

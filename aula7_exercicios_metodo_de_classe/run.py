from typing import Type

class Loja:

    taxa = 1.15

    def __init__(self, valor: Type[float]) -> Type[None]:
        self.__valor_produto_bruto = valor

    def consultar_valor_do_produto(self) -> Type[float]:
        return self.__valor_produto_bruto * self.taxa

    @classmethod
    def editar_taxa_do_produto(cls, valor: Type[float]) -> Type[None]:
        cls.taxa = valor


loja_praia = Loja(30.50)
loja_shopping = Loja(10.39)
loja_rua = Loja(20.33)

print(loja_praia.consultar_valor_do_produto())
print(loja_shopping.consultar_valor_do_produto())
print(loja_rua.consultar_valor_do_produto())

print('Editei a taxa!!!')
loja_praia.editar_taxa_do_produto(1.35)

print(loja_praia.consultar_valor_do_produto())
print(loja_shopping.consultar_valor_do_produto())
print(loja_rua.consultar_valor_do_produto())

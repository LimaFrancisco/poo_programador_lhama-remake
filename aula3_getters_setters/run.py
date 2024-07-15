class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None

    def set_valor(self, valor: int) -> None:
        self.__valor = valor
    
    def get_valor(self) -> int:
        return self.__valor


my_class = MinhaClasse()
# my_class.valor = 3 # ferindo o encapsulamento
valor = int(input('informe um valor: '))
my_class.set_valor(valor)
print(my_class.get_valor())

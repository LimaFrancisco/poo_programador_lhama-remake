class MinhaClasse:
    def __init__(self) -> None:
        self.__valor = None
        self.__elem = None

    def set_valor(self, valor: int) -> None:
        self.__valor = valor

    def get_valor(self) -> int:
        return self.__valor


my_class = MinhaClasse()
my_class.set_valor(123)
print(my_class.get_valor())
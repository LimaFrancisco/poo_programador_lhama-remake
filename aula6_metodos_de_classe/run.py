class MinhaClasse:

    estatico = 'lhama'           # variável de classe

    def __init__(self, estado) -> None:
        self.__estado = estado

    def print_variavel_de_classe(self):
        print(self.estatico)

    @classmethod
    def alteracao_da_variavel_de_classe(cls):   # alteração em nível de classe
        cls.estatico = 'algumaCoisa'
        # MinhaClasse.estatico = 'algumaCoisa'


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)
obj3 = MinhaClasse(True)

obj1.alteracao_da_variavel_de_classe()

print(obj1.estatico)
print(obj2.estatico)
print(obj3.estatico)
print(MinhaClasse.estatico)

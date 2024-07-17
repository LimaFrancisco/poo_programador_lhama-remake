class MinhaClasse:

        estatico = 'lhama'           # variável de classe

        def __init__(self, estado) -> None:
            self.__estado = estado

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(True)

MinhaClasse.estatico = 'programador' # alterando no contexto de classe
obj1.estatico = 'olaMundo'           # alterando no contexto de objeto
MinhaClasse.estatico = 'Lhamaaqui'   # alterando no contexto de classe

print(obj1.estatico)                 # contexto de objeto
print(obj2.estatico)                 # contexto de objeto
print(MinhaClasse.estatico)          # contexto de classe

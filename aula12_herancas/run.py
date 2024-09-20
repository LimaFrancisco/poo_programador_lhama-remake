from typing import Type

class Mamifero:
    def __init__(self, localizacao: Type[str]) -> Type[None]:
        self.localizacao = localizacao

    def andar(self) -> Type[None]:
        print(f'O animal está andando pelo {self.localizacao}')

class Cachorro(Mamifero):
    def __init__(self, localizacao: Type[str]) -> Type[None]:
        super().__init__(localizacao) # se refere a costrutor da classe superior

    def latir(self) -> Type[None]:
        print('O cachorro está latindo')
        self.andar()

class Gato(Mamifero):
    def __init__(self, localizacao: Type[str]) -> Type[None]:
        super().__init__(localizacao)
        
    def miar(self) -> Type[None]:
        print('O gato esta miando')
        self.andar()

dog = Cachorro('Chile')
dog.latir()

cat = Gato('Noruega')
cat.miar()


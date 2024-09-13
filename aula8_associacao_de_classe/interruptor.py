class Interruptor:

    # Constructor
    def __init__(self, comodo: str) -> NotImplemented:
        self.comodo = comodo

    # Methods
    def acender(self) -> None:
        print(f'Estou acendendo a luz do meu comodo: {self.comodo}')

    def apagar(self) -> None:
        print(f'Estou apagar a luz do meu comodo: {self.comodo}')

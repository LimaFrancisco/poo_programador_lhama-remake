from interruptor import Interruptor

class Pessoa:

    #Methods
    def acender_luzes(self, interruptor: Interruptor):
        interruptor.acender()

    def apagar_luzes(self, interruptor: Interruptor):
        interruptor.apagar()

    def dormir(self) -> None:
        print('A pessoa foi dormir.')
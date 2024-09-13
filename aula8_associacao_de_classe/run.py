from pessoa import Pessoa
from interruptor import Interruptor

pedro = Pessoa()
interruptor_sala = Interruptor('sala')
interruptor_quarto = Interruptor('quarto')

pedro.acender_luzes(interruptor_quarto)
pedro.apagar_luzes(interruptor_sala)
pedro.dormir()
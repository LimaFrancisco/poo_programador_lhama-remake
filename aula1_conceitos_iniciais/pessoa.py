class Pessoa:
    # consctrutor with some atributes
    def __init__(self, altura, idade):
        self.altura = altura
        self.idade = idade

    # methods
    def correr(self):
        print('Estou correndo...')

    def comer(self, alimento):
        print(f'Estou comendo {alimento}...')


pessoa = Pessoa(1.65, 19)
pessoa.correr()
pessoa.comer('carne')

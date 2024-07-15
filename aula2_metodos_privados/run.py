class Pessoa:
    # constructor
    def __init__(self, altura, cpf) -> None:
        self.altura = altura
        self.__cpf = cpf           # privete atribute 

    def apresentar(self):
        print(f'Ola! Minha altura - {self.altura}')
        self.__coletar_documento()

    
    def __coletar_documento(self): # private method 
        print(f'Meu documento - {self.__cpf}')



jorge = Pessoa('1.70', '4019238740')
jorge.apresentar()

from typing import Type

class Celular:
    def __init__(self, modelo: Type[str]) -> Type[None]:
        self.modelo = modelo
        
    def enviar_mensagem(self, mensagem: Type[str]) -> Type[None]:
        print(f'{mensagem}')

    def abrir_emails(self) -> Type[None]:
        print('Abrindo emails.')

    def abrindo_youtube(self) -> Type[None]:
        print('Abrindo Youtube.')

class Pessoa:
    def __init__(self, celular: Type[Celular]) -> Type[None]:
        self.__celular = celular

    def pedir_pizza(self, mensagem: Type[str]) -> Type[None]:
        self.__celular.enviar_mensagem(mensagem)

    def estudar(self) -> Type[None]:
        print('Estou estudando')



celular = Celular('Poco X6')
francisco = Pessoa(celular)
francisco.pedir_pizza('Me dê uma pizza pai...')

"""
SOLID - Acrônimo com principios e boas práticas em programação poo
S - Single Principle Responsability(Principio da responsabilidade única)
Um módulo deve um e apenas um motivo para alteração.
"""


class SistemaCadastral:
    
    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('Acessando o banco de dados...')
            print(f'Cadastrar usuario {nome}, idade{idade}')
        else:
            print('dados invalidos')

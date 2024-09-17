from typing import Type

class ConectorBancoDeDados:
    def __init__(self) -> Type[None]:
        self.connection = Type[None]

    def cenectar_ao_banco(self) -> Type[None]:
        self.cennection = True


class RepositorioDeBanco:
    def __init__(self, conexao: Type[ConectorBancoDeDados]) -> Type[None]:
        self.__conexao = conexao

    def busca_dados(self) -> Type[list]:
        if self.__conexao.connection:
            return [1, 2, 3, 4, 5]

        return None

class RegraDeNegocio:
    def __init__(self, repo: Type[RepositorioDeBanco]) -> Type[None]:
        self.__repo = repo 

    def calcular_resultados(self) -> Type[None]:
        dados = self.__repo.busca_dados()
        if not dados:
            print('Dados não encontrados. Verifique sua conexao com o banco')
        else:
            resposta = 0
            for dado in dados:
                resposta += dado
            print(f'o resultado e: {resposta}')


conn = ConectorBancoDeDados()
conn.cenectar_ao_banco()

repo = RepositorioDeBanco(conn)
regra = RegraDeNegocio(repo)

regra.calcular_resultados()

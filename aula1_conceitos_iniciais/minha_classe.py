class MinhaClasse:
    def __init__(self, info, alem): # metodo construtor é o primeiro!
        self.atributo1 = 'meu atributo'
        self.atributo2 = alem
        self.atributo3 = [1, 2, 'a']
        self.atributo_novo = info
        print(self.atributo_novo)

    def metodo_1(self):
        print('Minha ação 1')
        print('Minha ação 2')
        return 'Olá Mundo'

    def metodo_2(self, numero):
        self.metodo_1()
        print(self.atributo3[1] + numero)


minha_classe = MinhaClasse('info_do_contrutor', 213)

response = minha_classe.metodo_1()
print(response)
minha_classe.metodo_2(3)

class Pessoa():
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def saudacao(self):
        print(f'oi meu nome é {self.nome}, tenho {self.idade} anos e sou {self.profissao}')

pedro = Pessoa('Pedro', 25, 'reporter')
pedro.saudacao()

guilherme = Pessoa('Guilherme', 18, 'estudante')
guilherme.saudacao()

ewe = Pessoa('Ewelyn', 18, 'estudante')
ewe.saudacao()

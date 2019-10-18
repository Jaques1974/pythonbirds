class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome = None, idade = 35):#---->Aqui são parâmetros(None,35)para os valores(nome, idade).
        self.idade = idade  #----> Existem também os atributos de dados(que podem ser chamados também atributos de obje-
        self.nome = nome          #to) que são definidos pelo Método 'init'.Para criar o atributo de objeto, colocamos
        self.filhos = list(filhos) #'self' mais o ponto e seguido do nome do atributo.O que vem depois do sinal de igual
                                   # é o valor do atributo(aqui no:self.ATRIBUTO = VALOR)
    def cumprimentar(self):   #--->'cumprimentar' aqui, é chamado de Método(que definimos chamando a função 'def'), que
        return f'Ola {id(self)}'  #é uma espécie de atributo da classe Pessoa.


if __name__ == '__main__':
    renzo = Pessoa(nome='renzo') #--->Os filhos do objeto 'luciano' é um atributo complexo.Então para sermos bem especí-
    luciano= Pessoa(renzo, nome='Luciano') #ficos, já onde tinhamos a criação do objeto(p = Pessoa('luciano'),agora em
    print(Pessoa.cumprimentar(luciano)) #vez de 'p', vamos chamar o objeto de 'luciano' e entre parênteses onde tinha-
    print(id(luciano)) #mos o parâmetro 'luciano', vamos colocar primeiro o valor 'nome' seguido do parâmetro 'luciano'.
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:   #O que está escrito no for, se lê assim: Para cada filho dos filhos de luciano, im-
        print(filho.nome)          #prima o nome do filho.
    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.nome), id(renzo.nome))


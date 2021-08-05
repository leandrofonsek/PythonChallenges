from collections import deque

class ListaDeNodos(deque):
    def __init__(self):
        super().__init__()

    def imprimir(self):


class Nodo:
    def __init__(self,conteudo):
        self.conteudo = conteudo
        self.pai = None
        self.filhos = None

    def imprimir(self):
        print("{}".format(self.conteudo))
        if self.filhos:
            self.filhos.imprimir()

    def inserir_filhos(self, conteudo):
        if self.filhos == None:
            self.filhos = ListaDeNodos()
        filho = Nodo(conteudo)
        self.filhos.append(filho)

class Arvore:
    def __init__(self,conteudo):
        self.raiz = Nodo(conteudo)

    def imprimir(self):
        self.raiz.imprimir()

def main ():

    livraria = Arvore("Livros")
    livraria.imprimir()

    livraria.raiz.inserir_filhos("Gastronomia")
    livraria.raiz.inserir_filhos("Tecnologia")

    livraria.imprimir()

main()

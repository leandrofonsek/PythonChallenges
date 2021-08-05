from collections import deque


class Pilha:

    def __init__(self):
        self.pilha = deque()

    def empilha(self, valor):
        self.pilha.appendleft(valor)

    def desempilha(self):
        return self.pilha.popleft()

    @property
    def topo(self):
        return self.pilha[0]

    @property
    def vazia(self):
        if self.pilha:
            return False
        return True


def main():

    nomes = Pilha()
    nomes.empilha("Leandro")
    nomes.empilha("Karen")
    nomes.empilha("Thiego")
    nomes.empilha("Karina")
    nomes.empilha("Keivin")
    nomes.empilha("Carol")

    print(nomes.pilha)
    print(nomes.topo)
    print("Removendo topo: {}".format(nomes.desempilha()))
    print(nomes.topo)

main()
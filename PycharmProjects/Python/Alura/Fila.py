from collections import deque


class Fila:

    def __init__(self):
        self.fila = deque()

    def entrar(self, valor):
        self.fila.append(valor)

    def sair(self):
        return self.fila.popleft()

    @property
    def primeiro(self):
        return self.fila[0]

    @property
    def vazia(self):
        if self.fila:
            return False
        return True


def main():

    nomes = Fila()

    print("Vazia? {}".format(nomes.vazia))
    print("----------------")

    nomes.entrar("Leandro")
    nomes.entrar("Karen")
    nomes.entrar("Thiego")
    nomes.entrar("Karina")
    nomes.entrar("Keivin")
    nomes.entrar("Carol")
    print(nomes.fila)

    print("----------------")
    print("Vazia? {}".format(nomes.vazia))
    print("----------------")

    print(nomes.fila)
    quem_saiu = nomes.sair()
    print("----------------")
    print("Quem saiu: {}".format(quem_saiu))
    print(nomes.fila)

    print("----------------")
    print("Primeiro da fila: {}".format(nomes.primeiro))

    #print(nomes.topo)
    #print("Removendo topo: {}".format(nomes.desempilha()))
    #print(nomes.topo)

main()
class Celula:
    def __init__(self, conteudo):
        self.conteudo = conteudo
        self.proximo = None

class ListaLigada:

    def __init__(self):
        self.__inicio = None
        self.__quantidade = 0

    @property
    def inicio(self):
        return self.inicio

    @property
    def quantidade(self):
        return self.__quantidade

    def inserir_inicio(self,conteudo):
        celula = Celula(conteudo)
        celula.proximo = self.__inicio
        self.__inicio = celula
        self.__quantidade += 1

    def inserir(self,posicao,conteudo):
        if(posicao == 0):
            self.inserir_inicio(conteudo)
            return
        celula = Celula(conteudo)
        esquerda = self.__encontra_celula(posicao-1)
        celula.proximo = esquerda.proximo
        esquerda.proximo = celula
        self.__quantidade += 1

    def remover_inicio(self):
        removido = self.__inicio
        self.__inicio = removido.proximo
        removido.proximo = None
        self.__quantidade -= 1
        return removido.conteudo

    def remover(self,posicao):
        if(posicao == 0):
            self.remover_inicio()
            return
        esquerda = self.__encontra_celula(posicao - 1)
        removido = esquerda.proximo
        esquerda.proximo = removido.proximo
        removido.proximo = None
        self.__quantidade -= 1
        return removido.conteudo

    def __encontra_celula(self,posicao):
        self.__valida_posicao(posicao)
        atual = self.__inicio
        for i in range(0, posicao):
            atual = atual.proximo
        return atual

    def __valida_posicao(self,posicao):
        if 0 <= posicao <= self.__quantidade:
            return True
        print("Posicao invalida {}".format(posicao))
        exit(1)


    def imprimir(self):
        atual = self.__inicio
        for i in range(0, self.__quantidade):
            print("{}: {}".format(i,atual.conteudo))
            atual = atual.proximo

class Loja:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def __repr__(self):
        return "{}: {}".format(self.nome, self.endereco)

def main():
    loja1 = Loja("Loja1 Mercearia", "Rua das Laranjeiras, 12")
    loja2 = Loja("Loja2 Hortifruti", "Rua do Pomar, 300")
    loja3 = Loja("Loja3 Padaria", "Rua das Flores, 600")
    loja4 = Loja("Loja4 Supermercado", "Rua das Sésamo, 123")
    loja5 = Loja("Loja5 Barzinho", "Rua Alamo, 24")
    loja6 = Loja("Loja6 Quitanda", "Avenida Paes, 1291")

    lista = ListaLigada()
    lista.inserir_inicio(loja1)
    print("- Quantidade: {}".format(lista.quantidade))
    lista.imprimir()
    lista.inserir_inicio(loja2)
    print("- Quantidade: {}".format(lista.quantidade))
    lista.imprimir()
    lista.inserir_inicio(loja3)
    print("- Quantidade: {}".format(lista.quantidade))
    lista.imprimir()
    lista.inserir(1,loja4)
    print("- Quantidade: {}".format(lista.quantidade))
    lista.imprimir()
    lista.inserir(2,loja5)
    print("- Quantidade: {}".format(lista.quantidade))
    lista.imprimir()
    lista.inserir(lista.quantidade,loja6)
    print("- Quantidade: {}".format(lista.quantidade))
    lista.imprimir()


    removido = lista.remover_inicio()
    print("- Quantidade: {}".format(lista.quantidade))
    lista.imprimir()
    print("--> Removido: {}".format(removido))

    removido = lista.remover(2)
    print("- Quantidade: {}".format(lista.quantidade))
    lista.imprimir()
    print("--> Removido: {}".format(removido))

    removido = lista.remover(lista.quantidade - 1)
    print("- Quantidade: {}".format(lista.quantidade))
    lista.imprimir()
    print("--> Removido: {}".format(removido))


main ()

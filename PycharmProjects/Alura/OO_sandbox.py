class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo do titular {}: {}".format(self.__titular,self.__saldo))

    def deposita(self,valor):
        print("Depositando valor: {}".format(valor))
        self.__saldo += valor

    def __pode_sacar(self,valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def saca(self,valor):
        if(self.__pode_sacar(valor)):
            print("Sacando valor: {}".format(valor))
            self.__saldo -= valor
        else:
            print("Saldo insuficiente")

    def transfere(self,destino,valor):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        print("verificando limite")
        return self.__saldo

    @property
    def limite(self):
        print("verificando limite")
        return self.__limite

    @limite.setter
    def limite(self,valor):
        self.__limite = valor
        print("Novo Limite: {}".format(self.__limite))

    @staticmethod
    def codigo_banco():
        return "001"

class Data:
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatadata(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))


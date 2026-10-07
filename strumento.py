class Strumento:
    def __init__(self, codice, tipo, marca, anno_acquisto, valore):
        self.__codice = codice
        self.__tipo = tipo
        self.__marca= marca
        self.__anno_acquisto = anno_acquisto
        self.__valore = valore

    @property
    def codice(self):
        return self.__codice

    def __str__(self):

        return f'{self.__codice}, {self.__tipo}, {self.__marca}, {self.__anno_acquisto}, {self.__valore}'
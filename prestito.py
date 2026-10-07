class Prestito:
    def __init__(self, codice, data, id_strumento, cognome_allievo):
        self.__codice = codice
        self.__data = data
        self.__id_strumento = id_strumento
        self.__cognome_allievo = cognome_allievo

    @property
    def codice(self):
        return self.__codice

    @property
    def id_strumento(self):
        return self.__id_strumento

    def __str__(self):
        return f'{self.__codice}, {self.__data}, {self.__id_strumento}, {self.__cognome_allievo}'
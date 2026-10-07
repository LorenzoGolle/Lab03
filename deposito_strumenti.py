from asyncio import exceptions

from strumento import Strumento
from operator import attrgetter
from prestito import Prestito
class DepositoStrumenti:

    elenco_strumenti = []
    elenco_prestiti = []

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile

    def aggiorna_responsabile(self, nuovo_responsabile):
        self.responsabile = nuovo_responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""

        try:
            infile = open(file_path, "r")
            for line in infile:
                parti = line.split(',')
                s = Strumento(parti[0], parti[1], parti[2], parti[3], parti[4])
                self.elenco_strumenti.append(s)
        except FileNotFoundError:
            print("File non trovato")
        finally:
            infile.close()

    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        ultimo_strumento = self.elenco_strumenti[len(self.elenco_strumenti) - 1]
        ultimo_codice = ultimo_strumento.codice
        numero = int(ultimo_codice.lstrip('S'))
        nuovo_codice = 'S' + str(numero + 1)

        s = Strumento(nuovo_codice, tipo, marca, anno_acquisto, valore)
        self.elenco_strumenti.append(s)
        return s

    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        return sorted(self.elenco_strumenti, key=attrgetter('marca'))

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        trovato = False

        for strumento in self.elenco_strumenti:     #controllo che lo strumento esista
            if id_strumento == strumento.codice:
                trovato = True
        if not trovato:
            raise Exception('Lo strumento non esiste')

        for prestito in self.elenco_prestiti:       #controllo che lo strumento non sia già imprestato
            if id_strumento == prestito.id_strumento:
                raise Exception('Lo strumento è già stato prestato')

        i = 1
        codice = 'P' + str(i)
        for prestito in self.elenco_prestiti:       #aggiorno il codice
            if prestito.codice == codice:
                i+=1
                codice = 'P' + str(i)

        p = Prestito(codice, data, id_strumento, cognome_allievo)
        self.elenco_prestiti.append(p)

        return p

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        for prestito in self.elenco_prestiti:
            if prestito.codice == id_prestito:
                self.elenco_prestiti.remove(prestito)

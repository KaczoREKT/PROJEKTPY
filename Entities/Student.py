class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = {}
        

    def dodajOcene(self, kategoria, ocena):
        if kategoria in self.oceny:
            self.oceny[kategoria].append(ocena)
        else:
            self.oceny[kategoria] = [ocena]

    def usunOcene(self):
        pass
    
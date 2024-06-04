class Student:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko
        self.oceny = {}
        self.srednia_ocen = 0
        self.zagrozenie = "CZYSTY"
        self.nieobecnosci = 0
        self.obecnosci = 0

    def getImie(self):
        return self.imie

    def getNazwisko(self):
        return self.nazwisko

    def getCredencials(self):
        return str(self.imie + " " + self.nazwisko)
    
    def getObecnosci(self):
        return self.obecnosci
    
    def dodajObecnosc(self):
        self.obecnosci += 1
    def usunObecnosc(self):
        if self.obecnosci == 0:
            print("Exception")
        else:
            self.obecnosci -= 1
            

    def dodajOcene(self, ocena):
        if ocena.getKategoria() in self.oceny:
            self.oceny[ocena.getKategoria()].append(ocena)
            Student.czyZagrozony(self)
        else:
            self.oceny[ocena.getKategoria()] = [ocena]
            Student.czyZagrozony(self)

    def usunOcene(self):
        pass

    def getOceny(self):
        return [ocena for oceny in self.oceny.values() for ocena in oceny]

    def liczSrednia(self):
        if len(self.oceny) != 0:
            suma = 0
            for ocena in Student.getOceny(self):
                suma += int(ocena.getWartość())
            return suma / len(self.oceny)
        else:
            pass

    def dodajNieobecnosc(self):
        self.nieobecnosci += 1
        Student.czyZagrozony(self)
        print("nieobecnosc dziala")
    def usunNieobecnosc(self):
        if self.nieobecnosci == 0:
            print("Exception")
        else:
            self.nieobecnosci -= 1
            Student.czyZagrozony(self)
    def getNieobecnosci(self):
        return self.nieobecnosci

    def czyZagrozony(self):
        srednia = Student.liczSrednia(self)
        if srednia is not None:
            if srednia < 3 or self.nieobecnosci > 2:
                self.zagrozenie = "ZAGROŻENIE"
            else:
                self.zagrozenie = "CZYSTY"
                
    def getZagrozenie(self):
        return self.zagrozenie
            

class Ocena:
    def __init__(self, kategoria, wartość, waga, data):
        self.kategoria = kategoria
        self.wartość = wartość
        self.waga = waga
        self.data = data
        
    def getKategoria(self):
        return self.kategoria
    def getWartość(self):
        return self.wartość
    def setWartość(self, wartosc):
        self.wartość = wartosc
    def getWaga(self):
        return self.waga
    def getData(self):
        return self.data
import random
import os

import pandas as pd

from Entities.Student import Student


def generuj_studenta(plec):
    losowosc = random.randint(0, 39)
    plec_imie_txt = None
    plec_nazwisko_txt = None

    match plec:
        case 'M':
            plec_imie_txt = 'imionafacetuf.txt'
            plec_nazwisko_txt = "nazwiskafacetuf.txt"
        case 'K':
            plec_imie_txt = 'imionabab.txt'
            plec_nazwisko_txt = "nazwiskabab.txt"

    current_dir = os.path.dirname(os.path.dirname(__file__))  # Przejście do katalogu głównego PROJEKTPY
    path_imie = os.path.join(current_dir, 'TXT', plec_imie_txt)
    path_nazwisko = os.path.join(current_dir, 'TXT', plec_nazwisko_txt)

    # Zczytaj plik
    with open(path_imie, 'r', encoding='UTF-8') as plik:
        imiona = plik.read().replace('"', '').replace("'", '').strip()
    with open(path_nazwisko, 'r', encoding='UTF-8') as plik2:
        nazwiska = plik2.read().replace('"', '').replace("'", '').strip()
    lista_imion = imiona.split(',')
    lista_nazwisk = nazwiska.split(',')

    upieczony_student = Student(lista_imion[losowosc].strip(), lista_nazwisk[losowosc].strip())
    return upieczony_student


class Klasa:
    def __init__(self, numer_klasy, ilosc_kobiet, ilosc_mezczyzn):
        self.listaUczniow = []
        for i in range(ilosc_kobiet):
            nowy_student = generuj_studenta('K')
            self.listaUczniow.append(nowy_student)
        for i in range(ilosc_mezczyzn):
            nowy_student = generuj_studenta('M')
            self.listaUczniow.append(nowy_student)
        self.numer_klasy = numer_klasy
        

    def dodajUcznia(self, student):
        self.listaUczniow.append(student)
        
    def getListaUczniow(self):
        return self.listaUczniow
    def getNumerKlasy(self):
        return self.numer_klasy

    def generuj_statystyki(self):
        srednie_oceny = []
        nieobecnosci = []
        obecnosci = []
        for student in self.listaUczniow:
            srednia_ocen = student.liczSrednia()
            srednie_oceny.append(srednia_ocen)
            nieobecnosci.append(student.getNieobecnosci())
            obecnosci.append(student.getObecnosci())

        # Calculate class-wide statistics
        class_stats = {
            'Srednia_Ocen': {'value': sum(srednia_ocen for srednia_ocen in srednie_oceny if srednia_ocen is not None) / len(srednie_oceny) if any(srednie_oceny) else 0},
            'Srednia_Nieobecnosci': {'value': sum(nieobecnosci) / len(nieobecnosci) if nieobecnosci else 0},
            'Obecnosci': {'value': sum(obecnosci) if obecnosci else 0},
            'Nieobecnosci': {'value': sum(nieobecnosci) if nieobecnosci else 0}
         
        }

        return {
            'class_stats': class_stats
        }
        

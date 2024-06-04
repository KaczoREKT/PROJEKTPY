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
        # Prepare lists to collect data
        student_data = []
        for student in self.listaUczniow:
            oceny = student.getOceny()
            srednia_ocen = student.liczSrednia()
            nieobecnosci = student.getNieobecnosci()
            obecnosci = student.getObecnosci()
            zagrozenie = student.getZagrozenie()

            student_data.append({
                'Student': student.getCredencials(),
                'Srednia_Ocen': srednia_ocen,
                'Nieobecnosci': nieobecnosci,
                'Obecnosci': obecnosci,
                'Zagrozenie': zagrozenie
            })

        # Create a DataFrame from the collected data
        df = pd.DataFrame(student_data)

        # Group by student and compute statistics
        student_stats = df.groupby('Student').agg(
            Srednia_Ocen=pd.NamedAgg(column='Srednia_Ocen', aggfunc='mean'),
            Nieobecnosci=pd.NamedAgg(column='Nieobecnosci', aggfunc='sum'),
            Obecnosci=pd.NamedAgg(column='Obecnosci', aggfunc='sum'),
            Zagrozenie=pd.NamedAgg(column='Zagrozenie', aggfunc=lambda x: x.iloc[0])  # Assuming 'Zagrozenie' is a single value per student
        ).reset_index()

        # Compute overall class statistics
        class_stats = {
            'Srednia_Ocen': df['Srednia_Ocen'].mean(),
            'Nieobecnosci': df['Nieobecnosci'].sum(),
            'Obecnosci': df['Obecnosci'].sum(),
            'Zagrozenie': 'ZAGROŻENIE' if df['Zagrozenie'].str.contains('ZAGROŻENIE').any() else 'CZYSTY'
        }

        return {
            'student_stats': student_stats,
            'class_stats': class_stats
        }
        

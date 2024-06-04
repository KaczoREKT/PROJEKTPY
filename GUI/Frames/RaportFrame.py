import pandas as pd

from GUI.Button import Button
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Frames.Dziennik import Dziennik
from GUI.Label import Label
import tkinter as tk


class RaportFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Szefowa się ucieszy", font_size=100)
        self.label.pack(pady=100)

        self.button = Button(self, text="Generuj raport", command=lambda: self.generujRaport())
        self.button.pack(pady=self.pady, padx=self.padx)

    def generujRaport(self):
        data = []

        # Dodanie danych do listy
        for klasa in Dziennik.pobierzKlasy(self):
            for student in klasa.getListaUczniow():
                data.append([
                    klasa.numer_klasy,
                    student.getCredencials(),
                    student.getOceny(),
                    student.getObecnosci(),
                    student.getNieobecnosci()
                ])
    
        # Tworzenie DataFrame
        df = pd.DataFrame(data, columns=["Klasa", "Imię i Nazwisko", "Oceny", "Obecności", "Nieobecności"])
    
        # Zapisanie DataFrame do pliku Excel
        df.to_excel("report.xlsx", index=False)
    
        # Informacja o zakończeniu generowania raportu
        tk.messagebox.showinfo("Informacja", "Zrobiono report")
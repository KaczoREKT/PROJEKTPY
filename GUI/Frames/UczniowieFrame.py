from GUI.Button import Button
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Frames.Dziennik import Dziennik
from GUI.Label import Label
import tkinter as tk
from tkinter import ttk


class UczniowieFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Wybierz klasę", font_size=100)
        self.label.pack(pady=self.pady)

        self.listaklas = Dziennik.pobierzKlasy(self)
        for klasa in self.listaklas:
            # Do lambdy trzeba dodać parametr k ktory oznacza inną klasę
            self.button = Button(self, text=klasa.getNumerKlasy(),
                                 command=lambda k=klasa: self.nextFrame(KlasaFrame(k.getNumerKlasy())))
            self.button.pack(pady=self.pady, padx=self.padx)


class KlasaFrame(AbstractFrame):
    def eksmisja(self):
        pass
        # Funkcja która usunie studenta z uczelni tak o 

    def __init__(self, klasa):
        self.klasa = klasa
        super().__init__()
        self.listaklas = Dziennik.pobierzKlasy(self)

        self.tree = ttk.Treeview(self,
                                 columns=("imie", "nazwisko", "obecności", "nieobecności", "średnia", "zagrożenie"),
                                 show='headings')
        self.tree.heading("imie", text="Imię")
        self.tree.heading("nazwisko", text="Nazwisko")
        self.tree.heading("obecności", text="Obecności")
        self.tree.heading("nieobecności", text="Nieobecności")
        self.tree.heading("średnia", text="Średnia")
        self.tree.heading("zagrożenie", text="Zagrożenie")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.button = Button(self, text="EKSTERMINATOR STUDENTA", command=lambda: self.eksmisja())
        # Zapakuj gdy będzie gotowy

        for klasa in self.listaklas:
            if klasa.getNumerKlasy() == self.klasa:
                for student in klasa.getListaUczniow():
                    self.tree.insert("", "end", values=(student.getImie(), student.getNazwisko(),
                                                        student.getObecnosci(), student.getNieobecnosci(), student.liczSrednia(),
                                                        student.getZagrozenie()))

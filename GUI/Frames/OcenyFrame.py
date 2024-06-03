from GUI.Button import Button
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Frames.Dziennik import Dziennik
from GUI.Label import Label
import tkinter as tk


class OcenyFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Tryb niszczenia uczniów", font_size=100)
        self.label.pack(pady=self.pady)

        self.button = Button(self, text="Dodaj Ocenę", command=lambda: self.nextFrame(NoweOceny()))
        self.button.pack(pady=self.pady, padx=self.padx)

        self.button2 = Button(self, text="Historia Ocen", command=lambda: self.nextFrame(None))
        self.button2.pack(pady=self.pady, padx=self.padx)


class NoweOceny(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Szefowa się ucieszy", font_size=100)
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky="w")


        # Option Box dla Klasy
        self.klasy = [klasa.numer_klasy for klasa in Dziennik.pobierzKlasy(self)]
        self.selected_class = tk.StringVar(self) #sprawdz co to jest
        self.selected_class.set(self.klasy[0])

        self.class_menu = tk.OptionMenu(self, self.selected_class, *self.klasy)
        self.class_menu.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        # Option Box dla Studentów Klasy
        self.studenci = [klasa.listaUczniow for klasa in Dziennik.pobierzKlasy(self)]
        self.selected_student = tk.StringVar(self)
        self.selected_student.set(self.studenci[0])

        self.class_menu = tk.OptionMenu(self, self.selected_student, *self.studenci)
        self.class_menu.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        
        # Option Box dla rodzaju
        self.kategorie = ["Kolokwium", "Wejściówka", "Aktywność"]
        self.selected_category = tk.StringVar(self)
        self.selected_category.set(self.kategorie[0])
        
        self.kategoria_menu = tk.OptionMenu(self, self.selected_category, *self.kategorie)
        self.kategoria_menu.grid(row=0, column=2, padx=5, pady=5, sticky="w")

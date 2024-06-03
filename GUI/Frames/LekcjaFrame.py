from Entities.Klasa import Klasa
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Frames.Dziennik import Dziennik
from GUI.Label import Label
from GUI.Button import Button
import tkinter as tk



class LekcjaFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Wybierz Czynność", font_size=100)
        self.label.pack(pady=self.pady)

        self.button = Button(self, text="Nowa lekcja", command=lambda: self.nextFrame(NowaLekcja()))
        self.button.pack(pady=self.pady, padx=self.padx)

        self.button2 = Button(self, text="Zarządzaj Lekcjami", command=lambda: self.nextFrame(None))
        self.button2.pack(pady=self.pady, padx=self.padx)


class NowaLekcja(AbstractFrame):
    def __init__(self):
        super().__init__()
        klasy = Dziennik.pobierzKlasy(self)
        self.label = tk.Label(self, text="Wpisz datę lekcji")
        self.label.pack(pady=10, side=tk.TOP)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10, padx=10, side=tk.TOP)

        self.label2 = tk.Label(self, text="Wybierz klasę:")
        self.label2.pack(pady=10, side=tk.TOP)
        
        self.klasy = [klasa.numer_klasy for klasa in klasy]  
        self.selected_class = tk.StringVar(self)
        self.selected_class.set(self.klasy[0])

        self.class_menu = tk.OptionMenu(self, self.selected_class, *self.klasy)
        self.class_menu.pack(pady=10, padx=10, side=tk.TOP)

        data_lekcji = self.entry.get()
        klasa = self.selected_class.get()
        self.button = tk.Button(self, text="Dalej", command=lambda: self.nextFrame(Dziennik(data_lekcji, klasa)))
        self.button.pack(pady=10, side=tk.BOTTOM)

        
        

    
        



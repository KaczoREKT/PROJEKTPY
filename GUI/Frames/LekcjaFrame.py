from Entities.Klasa import Klasa
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Frames.Dziennik import Dziennik
from GUI.Label import Label
from GUI.Button import Button
import tkinter as tk


class LekcjaFrame(AbstractFrame):
    _listaLekcji = []

    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Wybierz Czynność", font_size=100)
        self.label.pack(pady=self.pady)

        self.button = Button(self, text="Nowa lekcja", command=lambda: self.nextFrame(NowaLekcja()))
        self.button.pack(pady=self.pady, padx=self.padx)

        self.button2 = Button(self, text="Zarządzaj Lekcjami", command=lambda: self.nextFrame(ZarzadzajLekcjami()))
        self.button2.pack(pady=self.pady, padx=self.padx)

    def getListaLekcji(self):
        return LekcjaFrame._listaLekcji

    def updateListaLekcji(self, dziennik):
        LekcjaFrame._listaLekcji.append(dziennik)



class NowaLekcja(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self, text="Wpisz datę lekcji")
        self.label.pack(pady=10, side=tk.TOP)

        self.entry = tk.Entry(self)
        self.entry.pack(pady=10, padx=10, side=tk.TOP)

        self.label2 = tk.Label(self, text="Wybierz klasę:")
        self.label2.pack(pady=10, side=tk.TOP)

        self.klasy = [klasa.numer_klasy for klasa in Dziennik.pobierzKlasy(self)]
        self.selected_class = tk.StringVar(self)
        self.selected_class.set(self.klasy[0])

        self.class_menu = tk.OptionMenu(self, self.selected_class, *self.klasy)
        self.class_menu.pack(pady=10, padx=10, side=tk.TOP)

        self.button = tk.Button(self, text="Dalej", command=self.on_button_click)
        self.button.pack(pady=10, side=tk.BOTTOM)

    def on_button_click(self):
        data_lekcji = self.entry.get()
        klasa = self.selected_class.get()

        if not any(d.klasa == klasa and d.data_lekcji == data_lekcji for d in LekcjaFrame.getListaLekcji(self)):
            nowyDziennik = Dziennik(data_lekcji, klasa)
            LekcjaFrame.updateListaLekcji(self, nowyDziennik)
            self.nextFrame(nowyDziennik)
        else:
            tk.messagebox.showinfo("Informacja", "Dziennik już istnieje dla danej klasy i daty")

    

class ZarzadzajLekcjami(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.lekcje_listbox = tk.Listbox(self, width=50)
        self.lekcje_listbox.pack(side=tk.LEFT)
        self.lekcje_listbox.delete(0, tk.END)
        for lekcja in LekcjaFrame.getListaLekcji(self):
            tk.messagebox.showinfo("Informacja", lekcja)
            self.lekcje_listbox.insert(tk.END, lekcja)

from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Label import Label
from GUI.Button import Button
import tkinter as tk
from tkinter import ttk


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

    def nextFrame(self, frameToShow):
        AbstractFrame._lastFrame = self
        self.pack_forget()
        frameToShow.pack()

    def __init__(self):
        super().__init__()
        self.entry = tk.Entry(self)
        self.entry.pack(pady=100, padx=100, side=tk.LEFT)

        self.entry2 = tk.Entry(self)
        self.entry2.pack(pady=10, padx=10, side=tk.LEFT)

        self.button = tk.Button(self, text="Dalej", command=lambda: self.nextFrame(Dziennik()))
        self.button.pack(pady=0, side=tk.BOTTOM)

        self.label = tk.Label(self, text="Wpisz datę oraz temat lekcji")
        self.label.pack(pady=10, side=tk.TOP)


class Dziennik(ttk.Frame):
    def __init__(self):
        # Ramka dla danych lekcji
        super().__init__()
        lekcja_frame = self

        # Etykiety i pola tekstowe dla danych lekcji
        ttk.Label(lekcja_frame, text="Data lekcji:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.data_lekcji_entry = ttk.Entry(lekcja_frame)
        self.data_lekcji_entry.grid(row=0, column=1, padx=5, pady=5, sticky="we")

        ttk.Label(lekcja_frame, text="Imię i Nazwisko ucznia:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.uczen_entry = ttk.Entry(lekcja_frame)
        self.uczen_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        # Ramka dla tabeli z obecnościami
        tabela_frame = ttk.LabelFrame(self, text="Tabela")
        tabela_frame.grid(row=1, column=0, padx=10, pady=5, sticky="we")

        # Tabela z obecnościami
        self.table = ttk.Treeview(tabela_frame, columns=("Imię", "Nazwisko", "Obecność", "Nieobecność", "Spóźnienie"))
        self.table.heading("#0", text="ID")
        self.table.heading("Imię", text="Imię")
        self.table.heading("Nazwisko", text="Nazwisko")
        self.table.heading("Obecność", text="Obecność")
        self.table.heading("Nieobecność", text="Nieobecność")
        self.table.heading("Spóźnienie", text="Spóźnienie")
        self.table.column("#0", width=50)
        self.table.column("Imię", width=100)
        self.table.column("Nazwisko", width=100)
        self.table.column("Obecność", width=100)
        self.table.column("Nieobecność", width=100)
        self.table.column("Spóźnienie", width=100)
        self.table.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Scrollbar
        scrollbar = ttk.Scrollbar(tabela_frame, orient="vertical", command=self.table.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.table.configure(yscroll=scrollbar.set)

        # Przyciski
        button_frame = ttk.Frame(self)
        button_frame.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        ttk.Button(button_frame, text="Dodaj ucznia", command=lambda: self.dodaj_ucznia()).grid(row=0, column=0, padx=5,
                                                                                                pady=5)
        ttk.Button(button_frame, text="Usuń ucznia", command=lambda: self.usun_ucznia()).grid(row=0, column=1, padx=5,
                                                                                              pady=5)
        ttk.Button(button_frame, text="Zapisz", command=lambda: self.zapisz_dziennik()).grid(row=0, column=2, padx=5,
                                                                                             pady=5)

    def dodaj_ucznia(self):
        imie = self.uczen_entry.get().split()[0]
        nazwisko = self.uczen_entry.get().split()[1]
        self.table.insert("", "end", text="1", values=(imie, nazwisko, "", "", ""))
        self.uczen_entry.delete(0, 'end')

    def usun_ucznia(self):
        if self.table.selection():
            selected_item = self.table.selection()[0]
            self.table.delete(selected_item)

    def zapisz_dziennik(self):
        # Tutaj można umieścić kod do zapisu danych dziennika
        pass

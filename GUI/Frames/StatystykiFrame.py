from Entities.Klasa import Klasa
from GUI.Frames.AbstractFrame import AbstractFrame
import pandas as pd
from tkinter import ttk
import tkinter as tk

from GUI.Frames.Dziennik import Dziennik


class StatystykiFrame(AbstractFrame):
    def update_statistics(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for klasa in self.klasy:
            stats = klasa.generuj_statystyki()

            # Insert new data into the treeview
            for key, value in stats['class_stats'].items():
                try:
                    srednia_ocen = value['Srednia_Ocen']['value']
                    nieobecnosci = value['Nieobecnosci']['value']
                    obecnosci = value['Obecnosci']['value']
                    zagrozenie = value['Zagrozenie']['value']
                    self.tree.insert('', 'end', values=(srednia_ocen, nieobecnosci, obecnosci, zagrozenie))
                except KeyError as e:
                    print(f"Missing key: {e}")
            # Update class stats label
            class_stats_text = (f"Srednia Ocen: {stats['class_stats']['Srednia_Ocen']}\n"
                                f"Średnia Nieobecności: {stats['class_stats']['Srednia_Nieobecnosci']}\n"
                                f"Całkowita Liczba Obecności: {stats['class_stats']['Obecnosci']}\n"
                                f"Całkowita Liczba Nieobecności: {stats['class_stats']['Nieobecnosci']}\n")

            self.class_stats_label.config(text=class_stats_text)

    def __init__(self):
        super().__init__()
        self.klasy = Dziennik.pobierzKlasy(self)
        self.tree = ttk.Treeview(self, columns=(
            'Srednia_Ocen', 'Srednia_Nieobecnosci', 'Nieobecnosci', 'Obecnosci'), show='headings')
        self.tree.heading('Srednia_Ocen', text='Średnia Ocen')
        self.tree.heading('Srednia_Nieobecnosci', text="Średnia Nieobecności")
        self.tree.heading('Nieobecnosci', text='Nieobecności')
        self.tree.heading('Obecnosci', text='Obecności')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.class_stats_label = tk.Label(self, text='', justify=tk.LEFT)
        self.class_stats_label.pack(fill=tk.BOTH, expand=True)

        self.update_button = tk.Button(self, text='Aktualizuj Statystyki', command=self.update_statistics)
        self.update_button.pack()

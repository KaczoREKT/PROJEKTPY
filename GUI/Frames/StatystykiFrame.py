from Entities.Klasa import Klasa
from GUI.Frames.AbstractFrame import AbstractFrame
import pandas as pd
from tkinter import ttk
import tkinter as tk

from GUI.Frames.Dziennik import Dziennik


class StatystykiFrame(AbstractFrame):
    def update_statistics(self):
        # Clear existing data in the treeview
        for row in self.tree.get_children():
            self.tree.delete(row)
        for klasa in self.klasy:
            stats = klasa.generuj_statystyki()
            print("Student Statistics:\n", stats['student_stats'])
            print("\nClass Statistics:\n", stats['class_stats'])


            # Insert new data into the treeview
            for index, row in stats['student_stats'].iterrows():
                self.tree.insert('', 'end', values=(row['Srednia_Ocen'], row['Nieobecnosci'], row['Obecnosci'], row['Zagrozenie']))

            # Update class stats label
            class_stats_text = (f"Średnia Ocen: {stats['class_stats']['Srednia_Ocen']}\n"
                                f"Nieobecności: {stats['class_stats']['Nieobecnosci']}\n"
                                f"Obecności: {stats['class_stats']['Obecnosci']}\n"
                                f"Zagrożenie: {stats['class_stats']['Zagrozenie']}")
            self.class_stats_label.config(text=class_stats_text)

    def __init__(self):
        super().__init__()
        self.klasy = Dziennik.pobierzKlasy(self)
        self.tree = ttk.Treeview(self, columns=('Srednia_Ocen', 'Nieobecnosci', 'Obecnosci', 'Zagrozenie'), show='headings')
        self.tree.heading('Srednia_Ocen', text='Średnia Ocen')
        self.tree.heading('Nieobecnosci', text='Nieobecności')
        self.tree.heading('Obecnosci', text='Obecności')
        self.tree.heading('Zagrozenie', text='Zagrożenie')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.class_stats_label = tk.Label(self, text='', justify=tk.LEFT)
        self.class_stats_label.pack(fill=tk.BOTH, expand=True)

        self.update_button = tk.Button(self, text='Aktualizuj Statystyki', command=self.update_statistics)
        self.update_button.pack()
        

        
            
        
        
    
from GUI.Frames.AbstractFrame import AbstractFrame
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
        self.entry = tk.Entry(self)
        self.entry.pack(pady=100, padx=100, side=tk.LEFT)

        self.entry2 = tk.Entry(self)
        self.entry2.pack(pady=10, padx=10, side=tk.LEFT)

        self.button = tk.Button(self, text="Dalej", command=lambda: self.nextFrame(None))
        self.button.pack(pady=0, side=tk.BOTTOM)

        self.label = tk.Label(self, text="Wpisz datę oraz temat lekcji")
        self.label.pack(pady=10, side=tk.TOP)

    def display_text(self):
        text = self.entry.get()  # Pobierz wprowadzony tekst z pola Entry
        self.label.config(text="Wprowadzony tekst: " + text)
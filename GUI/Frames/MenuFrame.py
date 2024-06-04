import tkinter as tk

from GUI.Frames.StatystykiFrame import StatystykiFrame
from GUI.Label import Label
from GUI.Button import Button
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Frames.LekcjaFrame import LekcjaFrame
from GUI.Frames.OcenyFrame import OcenyFrame
from GUI.Frames.UczniowieFrame import UczniowieFrame
from GUI.Frames.MailFrame import MailFrame
from GUI.Frames.RaportFrame import RaportFrame


class MenuFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Co dzisiaj chcesz zrobić?", font_size=100)
        self.label.pack(pady=self.pady)

        self.button = Button(self, text="Nowa \nLekcja", command=lambda: self.nextFrame(LekcjaFrame()))
        self.button.pack(pady=self.pady, padx=self.padx, side=tk.LEFT)

        self.button2 = Button(self, text="Oceny", command=lambda: self.nextFrame(OcenyFrame()))
        self.button2.pack(pady=self.pady, padx=self.padx, side=tk.LEFT)

        self.button3 = Button(self, text="Uczniowie", command=lambda: self.nextFrame(UczniowieFrame()))
        self.button3.pack(pady=self.pady, padx=self.padx, side=tk.LEFT)

        self.button4 = Button(self, text="Skrzynka\n Pocztowa", command=lambda: self.nextFrame(MailFrame()))
        self.button4.pack(pady=self.pady, padx=self.padx, side=tk.LEFT)

        self.button5 = Button(self, text="Generuj\n Raport", command=lambda: self.nextFrame(RaportFrame()))
        self.button5.pack(pady=self.pady, padx=self.padx, side=tk.LEFT)

        self.button6 = Button(self, text="Generuj\n Statystyki", command=lambda: self.nextFrame(StatystykiFrame()))
        self.button6.pack(pady=self.pady, padx=self.padx, side=tk.LEFT)

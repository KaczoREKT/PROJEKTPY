import tkinter as tk

from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Label import Label
from GUI.Button import Button


class MenuFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Co dzisiaj chcesz zrobić?", font_size=100)
        self.label.pack(pady=0)
        
        self.button = Button(self,text="Nowa \nLekcja")
        self.button.pack(pady=300, padx=100, side=tk.LEFT)

        self.button2 = Button(self,text="Oceny")
        self.button2.pack(pady=300, side=tk.LEFT)

        self.button3 = Button(self,text="Uczniowie")
        self.button3.pack(pady=300, padx=100, side=tk.LEFT)

        self.button4 = Button(self,text="Skrzynka Pocztowa")
        self.button4.pack(pady=300, padx=100, side=tk.LEFT)

        self.button5= Button(self,text="Generuj Raport")
        self.button5.pack(pady=300, padx=100, side=tk.BOTTOM)

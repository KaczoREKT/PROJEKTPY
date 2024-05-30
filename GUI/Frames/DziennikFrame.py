from tkinter import ttk
from GUI.Label import Label


class DziennikFrame(ttk.Frame):
    def __init__(self):
        super().__init__()
        self.label1 = Label(self, text="Dupa", font_size=100)
        self.label1.pack()

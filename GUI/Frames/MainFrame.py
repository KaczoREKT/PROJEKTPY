from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Frames.MenuFrame import MenuFrame
from GUI.Button import Button
from GUI.Label import Label
import tkinter as tk


class MainFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Dzień Dobry", font_size=100)
        self.label.pack(pady=100)

        self.button = Button(self, text="Nienawidzę tej pracy",
                             command=lambda: self.nextFrame(MenuFrame()))
        self.button.pack(pady=20, side=tk.TOP)

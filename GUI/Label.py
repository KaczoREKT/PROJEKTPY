import tkinter as tk
from tkinter import ttk

class Label(ttk.Label):
    def __init__(self, parent, text, font_family="Comic Sans MS", font_size=32, **kwargs):
        # Tworzenie stylu dla przycisku
        self.style_name = "Custom.TLabel"
        self.font = (font_family, font_size)
        style = ttk.Style()
        style.configure(self.style_name, font=self.font)

        super().__init__(parent, text=text, style=self.style_name, **kwargs)

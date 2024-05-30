from tkinter import ttk


class Button(ttk.Button):
    def __init__(self, parent, text, font_family="Comic Sans MS", font_size=32, command=None, **kwargs):
        self.style_name = "Custom.TButton"
        self.font = (font_family, font_size)
        style = ttk.Style()
        style.configure(self.style_name, font=self.font)

        # Inicjalizacja przycisku
        super().__init__(parent, text=text, command=command, style=self.style_name, **kwargs)

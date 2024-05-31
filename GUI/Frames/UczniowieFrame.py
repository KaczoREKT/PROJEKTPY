from GUI.Button import Button
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Label import Label


class UczniowieFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Wybierz klasę", font_size=100)
        self.label.pack(pady=self.pady)

        self.button = Button(self, text="2B", command=lambda: self.nextFrame(None))
        self.button.pack(pady=self.pady, padx=self.padx)

        

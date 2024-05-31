from GUI.Button import Button
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Label import Label


class OcenyFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Tryb niszczenia uczniów", font_size=100)
        self.label.pack(pady=self.pady)

        self.button = Button(self, text="Dodaj Ocenę", command=lambda: self.nextFrame(None))
        self.button.pack(pady=self.pady, padx=self.padx)

        self.button2 = Button(self, text="Historia Ocen", command=lambda: self.nextFrame(None))
        self.button2.pack(pady=self.pady, padx=self.padx)

        
from GUI.Button import Button
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Label import Label


class RaportFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Szefowa się ucieszy", font_size=100)
        self.label.pack(pady=100)

        self.button = Button(self, text="Generuj raport", command=lambda: self.nextFrame(None))
        self.button.pack(pady=self.pady, padx=self.padx)
        
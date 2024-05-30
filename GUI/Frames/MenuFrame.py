from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Label import Label


class MenuFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label1 = Label(self, text="Dupa", font_size=100)
        self.label1.pack()


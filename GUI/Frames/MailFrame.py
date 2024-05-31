from GUI.Button import Button
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Label import Label


class MailFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="NIE WYLOGOWAŁEŚ SIĘ!!!!", font_size=100)
        self.label.pack(pady=self.pady)

        self.button = Button(self, text="Utwórz Maila", command=lambda: self.nextFrame(None))
        self.button.pack(pady=self.pady, padx=self.padx)

        self.button2 = Button(self, text="Wysłane", command=lambda: self.nextFrame(None))
        self.button2.pack(pady=self.pady, padx=self.padx)

        self.button3 = Button(self, text="SPAM", command=lambda: self.nextFrame(None))
        self.button3.pack(pady=self.pady, padx=self.padx)
        
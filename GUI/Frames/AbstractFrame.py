from tkinter import ttk


class AbstractFrame(ttk.Frame):
    def __init__(self):
        super().__init__()

    def showFrame(self, frameToShow):
        self.pack_forget()
        frameToShow.pack()

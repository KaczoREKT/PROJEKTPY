import tkinter as tk
from GUI.Frames.MainFrame import MainFrame


class MyTk(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dziennik 6.6.6")
        self.geometry("1920x1080")
        mmm = MainFrame()
        mmm.pack()
        self.mainloop()

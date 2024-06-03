from tkinter import ttk
from GUI.Button import Button
import tkinter as tk


class AbstractFrame(ttk.Frame):
    _frameList = []


    def __init__(self):
        super().__init__()
        self.pady = 30
        self.padx = 10
        self.button = Button(self, text="Cofnij", command=lambda: self.previousFrame())
        self.button.pack(pady=self.pady, padx=self.padx, side=tk.BOTTOM)

    def previousFrame(self):
        if AbstractFrame._frameList[0] is not None:
            self.pack_forget()
            AbstractFrame._frameList[-1].pack()
            AbstractFrame._frameList.pop(-1)

    def nextFrame(self, frameToShow):
        AbstractFrame._frameList.append(self)
        self.pack_forget()
        frameToShow.pack()
        
    def getFrameList(self):
        return AbstractFrame._frameList
    
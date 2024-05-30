import tkinter

from Entities.Student import Student
from GUI.Frames.MainFrame import MainFrame
from GUI.MyTk import MyTk

Jacek = Student("Jacek", "Debil")
main = MyTk()

'''
root = tkinter.Tk()
root.title("Dziennik 6.6.6")
root.geometry("1920x1080")

frame = MainFrame()
frame.pack()

root.mainloop()
'''

print(Jacek.i)


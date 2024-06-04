from datetime import datetime

from Entities.Ocena import Ocena
from GUI.Button import Button
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Frames.Dziennik import Dziennik
from GUI.Label import Label
import tkinter as tk


class OcenyFrame(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Tryb niszczenia uczniów", font_size=100)
        self.label.pack(pady=self.pady)

        self.button = Button(self, text="Dodaj Ocenę", command=lambda: self.nextFrame(NoweOceny()))
        self.button.pack(pady=self.pady, padx=self.padx)

        self.button2 = Button(self, text="Historia Ocen", command=lambda: self.nextFrame(HistoriaOcen()))
        self.button2.pack(pady=self.pady, padx=self.padx)


class NoweOceny(AbstractFrame):
    def __init__(self):
        super().__init__()
        self.label = Label(self, text="Szefowa się ucieszy", font_size=100)
        self.label.pack(pady=100)

        self.button = Button(self, text="Aktualizuj", command=lambda: aktualizuj_studentow())
        self.button.pack(pady=0)

        # Option Box dla Klasy
        self.klasy = [klasa.numer_klasy for klasa in Dziennik.pobierzKlasy(self)]
        self.selected_class = tk.StringVar(self)  # sprawdz co to jest
        self.selected_class.set(self.klasy[0])

        self.class_menu = tk.OptionMenu(self, self.selected_class, *self.klasy)
        self.class_menu.pack(pady=10, padx=10, side=tk.TOP)

        def pobierz_studentow(klasa):
            return [str(student.getImie() + " " + student.getNazwisko()) for student in klasa.listaUczniow]

        def aktualizuj_studentow():
            selected_class_index = self.klasy.index(self.selected_class.get())
            students_for_selected_class = pobierz_studentow(Dziennik.pobierzKlasy(self)[selected_class_index])
            self.selected_student.set(students_for_selected_class[0])
            self.student_menu['menu'].delete(0, 'end')
            for student in students_for_selected_class:
                self.student_menu['menu'].add_command(label=student, command=tk._setit(self.selected_student, student))

        # Option Box dla Studentów Klasy
        self.selected_student = tk.StringVar(self)

        # Pobieranie listy studentów dla pierwszej klasy na liście jako domyślnej
        initial_students = pobierz_studentow(Dziennik.pobierzKlasy(self)[0])
        self.selected_student.set(initial_students[0])

        self.student_menu = tk.OptionMenu(self, self.selected_student, *initial_students)
        self.student_menu.pack(pady=10, padx=10, side=tk.TOP)

        # Option Box dla rodzaju
        self.kategorie = ["Praca Domowa", "Test", "Sprawdzian"]
        self.selected_category = tk.StringVar(self)
        self.selected_category.set(self.kategorie[0])

        self.kategoria_menu = tk.OptionMenu(self, self.selected_category, *self.kategorie)
        self.kategoria_menu.pack(pady=10, padx=10, side=tk.TOP)

        # Entry dla oceny
        self.entry = tk.Entry(self)
        self.entry.pack(pady=10, padx=10, side=tk.TOP)

        # Przycisk do dodania oceny
        self.button2 = Button(self, text="Dodaj", command=lambda: self.dodajOcene())
        self.button2.pack(pady=self.pady, padx=self.padx, side=tk.BOTTOM)

    def dodajOcene(self):
        wybranaWaga = None
        wybranaOcena = self.entry.get()
        wybranyStudent = self.selected_student.get()
        wybranyRodzajOceny = self.selected_category.get()

        match wybranyRodzajOceny:
            case "Praca Domowa":
                wybranaWaga = 3
            case "Test":
                wybranaWaga = 2
            case "Sprawdzian":
                wybranaWaga = 1

        for klasa in Dziennik.pobierzKlasy(self):
            for student in klasa.listaUczniow:
                credencials = str(student.getImie() + " " + student.getNazwisko())
                if credencials == wybranyStudent:
                    nowaOcena = Ocena(wybranyRodzajOceny, wybranaOcena, wybranaWaga, datetime.now().date())
                    student.dodajOcene(nowaOcena)
                    HistoriaOcen.dodajOcene(nowaOcena)
                    

                    tk.messagebox.showinfo("Informacja", str("Dodano ocenę dla " + credencials))
                    tk.messagebox.showinfo("Informacja", student.getOceny())
                    break


class HistoriaOcen(AbstractFrame):
    _lista_historii_ocen = []
    @staticmethod
    def dodajOcene(ocena):
        HistoriaOcen._lista_historii_ocen.append(ocena)
    
    def __init__(self):
        super().__init__()
        self.oceny_listbox = tk.Listbox(self, width=50)
        self.oceny_listbox.pack(side=tk.LEFT)
        self.oceny_listbox.delete(0, tk.END)
        for klasa in Dziennik.pobierzKlasy(self):
            for student in klasa.listaUczniow:
                for ocena in student.getOceny():
                    self.oceny_listbox.insert(tk.END, str(student.getCredencials() + " Ocena: " 
                                                          + ocena.getWartość() + " za: " + ocena.getKategoria()))
                                                    
    
        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.scrollbar.config(command=self.oceny_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
        self.oceny_listbox.config(yscrollcommand=self.scrollbar.set)
        
    
        

   
    



        
 
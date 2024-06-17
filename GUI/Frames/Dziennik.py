from tkinter import ttk, simpledialog
from Entities.Klasa import Klasa
from GUI.Button import Button
from GUI.Frames.AbstractFrame import AbstractFrame
from GUI.Label import Label


class Dziennik(ttk.Frame):
    _klasy = [Klasa("2B", 10, 20),
              Klasa("2C", 20, 1)]

    student_count = 0

    def __init__(self, data_lekcji, klasa):
        super().__init__()
        self.data_lekcji = data_lekcji
        self.klasa = klasa
        self.uczniowie = self.pobierzStudentow(klasa)

        Dziennik.student_count = len(self.uczniowie)  # Initialize student_count

        lekcja_frame = self

        # Etykiety i pola tekstowe dla danych lekcji
        Label(lekcja_frame, text="Data lekcji: " + data_lekcji).grid(row=0, column=0, padx=5, pady=5, sticky="w")

        # Ramka dla tabeli z obecnościami
        tabela_frame = ttk.LabelFrame(self, text="Tabela")
        tabela_frame.grid(row=1, column=0, padx=10, pady=5, sticky="we")

        # Entry na wpisanie ucznia do listy
        self.uczen_entry = ttk.Entry(tabela_frame)
        self.uczen_entry.grid(row=1, column=0, padx=10, pady=5, sticky="we")


        # Tabela z obecnościami
        self.table = ttk.Treeview(tabela_frame, columns=("Imię", "Nazwisko", "Obecność", "Nieobecność", "Spóźnienie"))
        self.table.heading("#0", text="ID")
        self.table.heading("Imię", text="Imię")
        self.table.heading("Nazwisko", text="Nazwisko")
        self.table.heading("Obecność", text="Obecność")
        self.table.heading("Nieobecność", text="Nieobecność")
        self.table.heading("Spóźnienie", text="Spóźnienie")
        self.table.column("#0", width=50)
        self.table.column("Imię", width=100)
        self.table.column("Nazwisko", width=100)
        self.table.column("Obecność", width=100)
        self.table.column("Nieobecność", width=100)
        self.table.column("Spóźnienie", width=100)
        self.table.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.table.bind("<Button-1>", self.on_double_click)

        # Scrollbar
        scrollbar = ttk.Scrollbar(tabela_frame, orient="vertical", command=self.table.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        self.table.configure(yscroll=scrollbar.set)

        # Przyciski
        button_frame = ttk.Frame(self)
        button_frame.grid(row=2, column=0, padx=10, pady=5, sticky="e")

        Button(button_frame, text="DODAJ SMARKACZA", command=lambda: self.dodaj_ucznia()).grid(row=0, column=0,
                                                                                               padx=5, pady=5)
        Button(button_frame, text="USUŃ SMARKACZA", command=lambda: self.usun_ucznia()).grid(row=0, column=1,
                                                                                             padx=5, pady=5)
        Button(button_frame, text="zapisz.", command=lambda: self.zapisz_dziennik()).grid(row=0, column=2, padx=5,
                                                                                          pady=5)
        Button(self, text="Cofnij", command=lambda: self.previousFrame()).grid(row=0, column=3, padx=5,
                                                                               pady=5)
        # Dodanie uczniów do tabeli
        self.load_students()

    def previousFrame(self):
        if AbstractFrame.getFrameList(self)[0] is not None:
            self.pack_forget()
            AbstractFrame.getFrameList(self)[-1].pack()

    def pobierzStudentow(self, class_number):
        for klasa in Dziennik._klasy:
            if klasa.numer_klasy == class_number:
                return klasa.listaUczniow
        return []

    def load_students(self):
        for idx, student in enumerate(self.uczniowie):
            self.table.insert("", "end", text=str(idx + 1), values=(student.imie, student.nazwisko, "", "", ""))

    def on_double_click(self, event):
        item = self.table.selection()[0]
        column = self.table.identify_column(event.x)
        if column:
            column_index = int(column.replace("#", "")) - 1
            self.edit_cell(item, column_index)

    def edit_cell(self, item, column):
        old_value = self.table.item(item, "values")[column]
        column_name = self.table.heading("#" + str(column + 1))["text"]
        new_value = simpledialog.askstring("Edytuj", f"Wpisz nową wartość dla kolumny '{column_name}':",
                                           initialvalue=old_value)
        if new_value is not None:
            values = list(self.table.item(item, "values"))
            values[column] = new_value
            self.table.item(item, values=values)

    def pobierzKlasy(self):
        return Dziennik._klasy

    def dodaj_ucznia(self):
        imie = self.uczen_entry.get().split()[0]
        nazwisko = self.uczen_entry.get().split()[1]
        Dziennik.student_count += 1
        self.table.insert("", "end", text=str(Dziennik.student_count), values=(imie, nazwisko, "", "", ""))
        self.uczen_entry.delete(0, 'end')

    def usun_ucznia(self):
        if self.table.selection():
            selected_item = self.table.selection()[0]
            self.table.delete(selected_item)

    def zapisz_dziennik(self):
        # Tutaj można umieścić kod do zapisu danych dziennika
        pass

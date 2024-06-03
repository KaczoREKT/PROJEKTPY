from GUI.Oceny.OcenaAbstract import OcenaAbstract


class Kolokwium(OcenaAbstract):
    def __init__(self):
        super().__init__()
        self.waga = 3
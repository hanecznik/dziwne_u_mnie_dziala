Class ptak:
    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def lec(self):
        print("Tutaj", self.gatunek, "zaraz osiągnie szybkosc", self.szybkosc)


Class orzel(ptak):
    def poluj(self):
        print("Tutaj", self.gatunek, "Polowanko")


Class pingwin(ptak):
    def slizgaj(self):
        print("Tutaj", self.gatunek, "Ślizganko")

    def lec(self):
        print("Tutaj", self.gatunek, "Niestety, nie umiem :( ")


orzel = orzel("orzel", 60)
pingwin = pingwin("pingwin", 3)

orzel.lec()
pingwin.lec()
orzel.poluj()
pingwin.slizgaj()
print()

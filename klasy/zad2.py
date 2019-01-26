class Employee:
    def __init__(self, imie, nazwisko, placa):
        self.imie = imie
        self.nazwisko = nazwisko
        self.placa = float(placa)
        self.czas_pracy = float(0)
        self.nadgodziny = float(0)

    def register_time(self, czas):
        if czas <= 8:
            self.czas_pracy += czas
        else:
            self.nadgodziny += (czas - 8)
            self.czas_pracy+=8

    def pay_salary(self):
        zaplata=self.czas_pracy * self.placa + self.nadgodziny * self.placa *1.5
        print(zaplata)
        self.czas_pracy = float(0)
        self.nadgodziny = float(0)

franek = Employee("Jan", "Nowak", 100.00)
print(franek.czas_pracy)
franek.register_time(10)
print(franek.czas_pracy)
print(franek.nadgodziny)
franek.pay_salary()
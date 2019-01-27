import random
class Postac:
    def __init__(self, imie, max_zdrowie, _atak):
        self.imie = imie
        self.max_zdrowie = max_zdrowie
        self.zdrowie = max_zdrowie
        self._atak = _atak
        self.ekwipunek = []

    @property
    def atak(self):
        dmg=self._atak
        for item in self.ekwipunek:
            dmg+=item.bonus_do_ataku
        return dmg

    def otrzymaj_obrazenia(self, dmg):
        self.zdrowie -= dmg

    def wylecz(self, hp):
        self.zdrowie += hp
        if self.zdrowie > self.max_zdrowie:
            self.zdrowie = max_zdrowie

    def daj_przedmiot(self,item):
        self.ekwipunek.append(item)

    def zabierz_przedmiot(self,item):
        for przerdmiot in self.ekwipunek:
            if przerdmiot==item:
                self.ekwipunek.remove(item)
    def czy_zyje(self):
        if self.zdrowie>0:
            return True
        return False
    def moc_ataku(self):
        return random.randrange(self.atak/2, self.atak)

    def __str__(self):
        result=f"Jestem {self.imie} mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} punktow zycia\nEkwipunek:\n"
        for element in self.ekwipunek:
            result+=f"{element.nazwa}, {element.bonus_do_ataku}\n"
        return result


def walka(first, second):
        def walnij(who,dmg):
            who.zdrowie-=dmg
            print(f"{who.imie} oberwal za {dmg}")
            if who.zdrowie<=0:
                print(f"i przegral")
                return True
        print(f"{first}\n{second}")
 #       while True:
 #           if walnij(second, first.moc_ataku()):
 #               break
 #           if walnij(first,second.moc_ataku()):
 #               break

        while not walnij(second, first.moc_ataku()) and not walnij(first,second.moc_ataku()):
            pass


def bojka(*args):
    for uderzajacy in args:
        who_got_hit==uderzajacy
        while not who_got_hit==uderzajacy:
            who_got_hit=random.choice(args)

 b  def __init__(self, nazwa, bonus_do_ataku):
        self.nazwa = nazwa
        self.bonus_do_ataku = bonus_do_ataku


def test_atak():
    postac = Postac("rafal", 5, 20)
    assert postac.zdrowie == 5
    postac.otrzymaj_obrazenia(1)
    assert postac.zdrowie == 4
    miecz=Przedmiot("miecz",100)
    assert miecz.nazwa=="miecz"
    assert postac.atak==20
    postac.daj_przedmiot(miecz)
    assert postac.atak==120
    postac.zabierz_przedmiot(miecz)
    assert postac.atak == 20
    assert postac.czy_zyje
postac = Postac("rafal", 100, 20)
miecz=Przedmiot("miecz",1)
postac.daj_przedmiot(miecz)
czapka=Przedmiot('czapka', 1)
postac.daj_przedmiot(czapka)
#print(postac.moc_ataku())
#print(postac)
postac2 = Postac("grzegorz", 100, 10)
walka(postac,postac2)
bojka(postac,postac2)
class Konwerter:
    @staticmethod
    def fahr_to_cel(val):
        cel = (val-32)*5/9
        return cel


assert Konwerter.fahr_to_cel(32) == 0
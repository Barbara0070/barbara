class Product:
    def __init__(self, id, produkt, cena):
        self.id=id
        self.produkt=produkt
        self.cena=cena
    def print_info(self):
        print(f"Produkt: {self.produkt}, id: {self.id}, cena: {self.cena} PLN")
    def __str__(self):
        return (f"Produkt: {self.produkt}, id: {self.id}, cena: {self.cena} PLN")

procukt=Product(1, 'woda', 12.20)
procukt.print_info()
print(procukt)
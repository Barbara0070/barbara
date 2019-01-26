# class Basket:
#    def __init__(self, count, product, price):
#        self.shop_list={
#            self.product : [count, price]
#        }
#    def count_total_price(self):
#        cost=0.00
#        for a in shop_list:
#            cost+=a.count*a.price
# kosz=Basket()
class Product:
    def __init__(self, count, product, price):
        self.count = count
        self.product = product
        self.price = price
class Basket:
    def __init__(self):
        self.entries=[]
    def add_product(self, product, count):
        flag=False
        for a in self.entries:
            if a[0].product==product:
                a.count+=count
                flag=True
        if flag==False:
            self.entries.append([product, count])
    def count_total_price(self):
        to_pay=0
        for a in self.entries:
            to_pay+=(a[0].price*a[1])
        return to_pay
    def generate_report(self):
        print(f"produkty w koszyku:\n")
        for i in range(len(self.entries)):
            print(f"{self.entries[i][0].product} cena:{self.entries[i][0].price} x {self.entries[i][1]}")
        print(f"koszt to {basket.count_total_price()}")


basket = Basket()
product = Product(1, "woda", 10.00)
basket.add_product(product, 5)
basket.add_product(product, 5)

print(basket.entries[0][0].price)
print(basket.count_total_price())
basket.generate_report()
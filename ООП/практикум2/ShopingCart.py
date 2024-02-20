class ShoppingCart:
    def __init__(self):
        self.tovars = []

    def add_item(self,name,count):
        self.tovars.append((name,count))

    def remove_item(self,name):
        for tovar in self.tovars:
            if tovar[0] == name:
                self.tovars.remove(tovar)
                break

    def calculate_total(self):
        total_quantity = sum(tovar[1] for tovar in self.tovars)
        return total_quantity

cart = ShoppingCart()
cart.add_item("Картофель", 100)
cart.add_item("Капуста", 200)
cart.add_item("Апельсин", 150)
print("Число товаров в корзине:") 

for tovar in cart.tovars:
    print(tovar[0], "-", tovar[1])

total_qty = cart.calculate_total()
print("Общее количество:", total_qty)
cart.remove_item("Апельсин")
print("\ОбновлениечислапокупоквКорзине после удаления апельсина:")

for tovar in cart.tovars:
    print(tovar[0], "-", tovar[1])
total_qty = cart.calculate_total()
print("Общее количество:", total_qty)
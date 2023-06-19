class Recipe():
    def __init__(self, dish, items, time):
        self.dish = dish
        self.items = items
        self.time = time

    def contents(self):
        print("The " + self.dish + " has " +  str(self.items) + " and takes " + str(self.time) + " minutes")


pizza = Recipe("Pizza", ['cheese', 'bread', 'tomato', 'pepperoni'], 45)
pasta = Recipe("Pasta", ['spaghetti', 'sauce', 'oregano'], 30)

print(pizza.items)
print(pizza.time)
print(pizza.contents())

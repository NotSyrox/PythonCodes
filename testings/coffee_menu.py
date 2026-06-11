class CoffeeMenu:
    def __init__(self):
        self.menu = {
        'espresso': 2.50,
        'latte': 2.75,
        'cappuccino': 3.20,
        'americano': 2.70
        }
    def get_price(self, key):
        return self.menu.get(key)


    def add_item(self, key, value):
        self.menu[key] = value
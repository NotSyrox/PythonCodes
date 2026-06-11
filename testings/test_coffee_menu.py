import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu1 = CoffeeMenu()

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu1.get_price("latte"), 2.75)

    def test_get_price_non_existing_item (self):
        self.assertEqual(self.menu1.get_price("test_coffee"), None)

    def test_add_item(self):
        self.menu1.add_item("test_coffee",10)
        self.assertEqual(self.menu1.get_price("test_coffee"),10)
        
if __name__ == "__main__":
    unittest.main()
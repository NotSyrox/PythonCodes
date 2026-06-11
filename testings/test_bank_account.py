import unittest
from bank_account import acc1, BankAccount

class TestBankAccount(unittest.TestCase):
    def test_initial_balance(self):
        self.assertEqual(acc1.balance,100)
    def setUp(self):
        self.account = BankAccount()
    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.balance,200)
    def test_withdraw(self):
        self.account.withdraw(50)
        self.assertEqual(self.account.balance,50)
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)
    def tearDown(self):
        self.account = None
if __name__ == '__main__':
    unittest.main()
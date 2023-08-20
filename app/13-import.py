import pandas as pd
import numpy as np
import sys
sys.path.append('/home/dasxgo/dev/exc/src')
import utils

utils

print('='*64)

if __name__ == '__main__':

    class Bank:
        def __init__(self):
            self.balance = 0
        
        def deposit(self, amount):
            self.balance += amount
            return self.balance
        
        def withdraw(self, amount):
            if amount <= self.balance:
                self.balance -= amount
            else:
                print('insufficient balance')
            return self.balance

my_bank = Bank()
print(f'deposit balance account  => ', my_bank.deposit(500))
print(f'withdraw balance account  => ', my_bank.withdraw(200))
print('='*64)
print(f'final account balance => ', my_bank.balance)




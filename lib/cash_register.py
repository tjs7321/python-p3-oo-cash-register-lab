#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, item, price, quantity=1):
    self.items.extend([item for i in range(quantity)])
    self.total = self.total + (price*quantity)
    self.last_transaction = [item, price, quantity]
  
  def apply_discount(self):
    if (self.discount == 0):
      print("There is no discount to apply.")
    else:
      self.total = self.total-(self.total*(self.discount/100))
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    del self.items[len(self.items)-self.last_transaction[2]:]
    self.total = self.total - (self.last_transaction[1]*self.last_transaction[2])
    
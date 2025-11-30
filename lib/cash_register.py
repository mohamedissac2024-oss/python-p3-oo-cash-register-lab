#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_items = []
        self.last_total = 0.0

    def add_item(self, title, price, quantity=1):
        self.last_items = [title] * quantity
        self.last_total = price * quantity
        self.total += self.last_total
        self.items.extend(self.last_items)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100.0)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_total > 0:
            self.total -= self.last_total
            for _ in range(len(self.last_items)):
                self.items.pop()
            self.last_total = 0.0
            self.last_items = []

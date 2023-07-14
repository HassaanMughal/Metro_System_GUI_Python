from tkinter import messagebox

class Card:
    def __init__(self, card_id, holder_name):
        self.card_id = card_id
        self.holder_name = holder_name
        self.card_balance = 0

    def get_id(self):
        return self.card_id

    def recharge(self, amount):
        self.card_balance += amount

    def get_balance(self):
        return self.card_balance

    def set_balance(self, balance):
        self.card_balance = balance    

    def make_payment(self, amount):
        if self.card_balance < amount:
            return False

        self.card_balance -= amount
        return True

    def display_info(self):
        messagebox.showinfo("Card Information", f"Card Number: {self.card_id}\nCard Holder Name: {self.holder_name}\nAvailable Balance: Rs.{self.card_balance}")
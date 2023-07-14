from tkinter import messagebox, simpledialog
from Ticket import Ticket
from Card import Card


class MetroTicketingSystem:
    def __init__(self):
        self.cards = []
        self.tickets = []
        self.price_km = 5
        self.card_id_counter = 1
        self.ticket_id_counter = 1

    def purchase_card(self):
        payment = 130
        response = messagebox.askyesno("Card Purchase", f"New Card Price: Rs. {payment}\nDo you want to purchase a card?")
        if response:
            cash_payment = simpledialog.askfloat("Payment", "Enter the payment amount:")

            while cash_payment < payment:
                messagebox.showerror("Insufficient Funds", f"Insufficient funds. Please input sufficient amount of money (Rs. {payment - cash_payment}).")
                cash_payment += simpledialog.askfloat("Payment", "Enter More Money:")

            change = cash_payment - payment
            holder_name = simpledialog.askstring("Name", "Enter Card Holder Name:")
            card = Card(str(self.card_id_counter), holder_name)
            self.cards.append(card)
            messagebox.showinfo("Card Purchase", f"Card purchased successfully. Please Collect your change Rs. {change}")
            card.display_info()
            self.card_id_counter += 1

    def buy_ticket(self, source, destination):
        distance = self.calculate_distance(source, destination)
        price = distance * self.price_km
        response = messagebox.askyesno("Ticket Purchase", f"Ticket Price: Rs. {price}\nDo you want to purchase the ticket?")

        if response:
            payment_method = simpledialog.askinteger("Payment Method", "Choose payment method:\n1. Cash\n2. Card\nEnter your choice:")

            if payment_method == 1:  # Cash payment
                payment = simpledialog.askfloat("Cash Payment", "Enter the payment amount:")

                while payment < price:
                    # messagebox.showerror("Insufficient Funds", f"Insufficient funds. Please input sufficient amount of money (Rs. {price - payment}).")
                    payment += simpledialog.askfloat("Cash Payment", f"Enter More Money (Rs. {price - payment}).")

                change = payment - price
                ticket = Ticket(self.ticket_id_counter, source, destination, distance, price)
                self.ticket_id_counter += 1
                self.tickets.append(ticket)
                messagebox.showinfo("Ticket Purchase", f"Ticket Purchased Successfully \nTicket ID: {ticket.ticket_id}\nSource: Station {ticket.source}\nDestination: Station {ticket.destination}\nDistance: {ticket.distance} km\nTicket Price: Rs.{ticket.price}\nPlease Collect your change Rs.{change}")
                return ticket


            elif payment_method == 2:  # Card payment
                card_id = simpledialog.askstring("Card Payment", "Enter your card number:")
                card = self.get_card_by_id(card_id)

                if card is None:
                    messagebox.showerror("Card Not Found", "Card not found. Please try again.")
                    return None

                if card.get_balance() < price:
                    response = messagebox.askyesno("Insufficient Funds", "Insufficient funds in the card. Would you like to recharge?")
                    if response:
                        bal = card.get_balance()
                        while bal < price:
                            bal += simpledialog.askfloat("Cash Payment", f"Enter More Money (Rs. {price - bal}).")
                            if bal is None:
                                return None
                        amount = bal - price        
                        card.set_balance(amount)
                    else:
                        return None

                card.make_payment(price)
                ticket = Ticket(self.ticket_id_counter, source, destination, distance, price)
                self.ticket_id_counter += 1
                self.tickets.append(ticket)
                messagebox.showinfo("Ticket Purchase", f"Ticket ID: {ticket.ticket_id}\nSource: Station {ticket.source}\nDestination: Station {ticket.destination}\nDistance: {ticket.distance} km\nTicket Price: Rs.{ticket.price}\nRemaining Card Balance: Rs.{card.get_balance()}")
                return ticket

            else:
                messagebox.showerror("Payment Method", "Invalid payment method. Please try again.")
                return None

    def calculate_distance(self, source, destination):
        return abs(destination - source) * 4

    def get_ticket_by_id(self, ticket_id):
        for ticket in self.tickets:
            if ticket.ticket_id == ticket_id:
                return ticket
        return None

    def get_card_by_id(self, card_id):
        for card in self.cards:
            if card.get_id() == card_id:
                return card
        return None

    def cancel_ticket(self, ticket_id):
        ticket = self.get_ticket_by_id(ticket_id)
        if ticket:
            refund_amount = ticket.price
            self.tickets.remove(ticket)
            return refund_amount
        return None

    def view_ticket_information(self, ticket_id):
        ticket = self.get_ticket_by_id(ticket_id)
        if ticket:
            messagebox.showinfo("Ticket Details", f"Ticket ID: {ticket.ticket_id}\nSource: Station {ticket.source}\nDestination: Station {ticket.destination}\nDistance in KM: {ticket.distance} km\nTicket Price: Rs.{ticket.price}")
        else:
            messagebox.showerror("Ticket Not Found", f"Ticket ID {ticket_id} not found.")

    def calculate_total_revenue(self):
        total_revenue = sum(ticket.price for ticket in self.tickets)
        return total_revenue

    def calculate_average_ticket_price(self):
        total_tickets = len(self.tickets)
        if total_tickets == 0:
            return 0
        total_price = sum(ticket.price for ticket in self.tickets)
        average_price = total_price / total_tickets
        return average_price
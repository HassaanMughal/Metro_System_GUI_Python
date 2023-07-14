class Ticket:
    def __init__(self, ticket_id, source, destination, distance, price):
        self.ticket_id = ticket_id
        self.source = source
        self.destination = destination
        self.distance = distance
        self.price = price

    def get_price(self):
        return self.price
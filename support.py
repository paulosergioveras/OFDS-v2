class Support():
    def __init__(self):
        self.tickets = []

    def create_ticket(self, customer, issue, comment):
        ticket = {
            'customer': customer,
            'issue': issue,
            'comment': comment,
            'status': 'open'
        }
        self.tickets.append(ticket)

    def close_ticket(self, customer):
        for ticket in self.tickets:
            if ticket['customer'] == customer and ticket['status'] == 'open':
                ticket['status'] = 'closed'
                print(f'Customer ticket {customer} closed.')
                return
        print(f'No open tickets found for the customer {customer}.')

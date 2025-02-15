from payments import Payment


class Orders():
    def __init__(self, order_id, customer, restaurant):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant
        self.items = {}
        self.status = 'Preparing'
        self.payment_status = 'Pending'

    def update_status(self, new_status):
        self.status = new_status

    def add_item(self, item, amount):
        if item is not self.restaurant.menu:
            return (f'The item "{item}" is not on the menu.')
        if item in self.items:
            self.items[item] += amount
        else:
            self.items[item] = amount

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def update_amount(self, item, new_amount):
        if item in self.items:
            self.items[item] = new_amount

    def show_order(self):
        print(f'Order ID: {self.order_id}')
        print(f'Customer: {self.customer}')
        print(f'Restaurant: {self.restaurant.name}')
        print(f'Status: {self.status}')
        print(f'Payment status: {self.payment_status}')
        print('Items:')

        total_price = 0

        for item, amount in self.items.items():
            if item in self.restaurant.menu:
                price = self.restaurant.menu[item]
                total_item = price * amount
                total_price += total_item
                print(f'- {item}: {amount} x R${price:.2f} = R${total_item:.2f}')
            else:
                print(f'- {item}: The item is not on the menu.')

        print(f'Total Price: R${total_price:.2f}')

    def process_payment(self, payment_method, payment_detail):
        process = Payment()
        self.payment_status = process.process_payment(self, payment_method, payment_detail)
        print(f'Payment Status: {self.payment_status}')


class OrderHistory():
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_order_list(self):
        return self.orders

    def reorder(self, order_id, customer, restaurant):
        for order in self.orders:
            if order.order_id == order_id:
                new_order = Orders(order_id, customer, restaurant)
                new_order.items = order.items.copy()
                return new_order
        print(f'Order with ID {order_id} not found.')
        return None

# Order Placement and Management
from restaurants import Restaurant

class Orders():
    def __init__(self, order_id, customer, restaurant):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant
        self.item = {}
        self.status = "Preparing"


    def update_status(self, new_status):
        self.status = new_status

    
    def add_item(self, item, amount):
        if item in self.item:
            self.item[item] += amount
        else:
            self.item[item] = amount

    
    def remove_item(self, item):
        if item in self.item:
            del self.item[item]

    
    def update_amount(self, item, new_amount):
        if item in self.item:
            self.item[item] = new_amount

    
    def show_order(self):
        print(f'Order ID: {self.order_id}')
        print(f'Customer: {self.customer}')
        print(f'Restaurant: {self.restaurant.name}')
        print(f'Status: {self.status}')
        print(f'Items:')
        
        total_price = 0

        for item, amount in self.item.items():
            if item in self.restaurant.menu:
                price = self.restaurant.menu[item]
                total_item = price * amount
                total_price += total_item
                print(f'- {item}: {amount} x R${price:.2f} = R${total_item:.2f}')
            else:
                print(f'- {item}: Item não encontrado no menu.')
        
        print(f'Total Price: R${total_price:.2f}')

    


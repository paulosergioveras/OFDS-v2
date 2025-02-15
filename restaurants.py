class Restaurant():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.menu = {}
        self.reviews = []

    def add_menu_item(self, item, price):
        if item in self.menu:
            return 'Item already added in menu.'
        else:
            self.menu[item] = price

    def remove_menu_item(self, item, price):
        if item not in self.menu:
            return 'This item is already deleted.'
        else:
            del self.menu[item]

    def update_item_price(self, item, new_price):
        if item in self.menu:
            self.menu[item] = new_price

    def add_review(self, review):
        self.reviews.append(review)

    def display_reviews(self):
        print('Restaurant Reviews:')
        for review in self.reviews:
            review.show_review()


class RestaurantAnalytics:
    def __init__(self):
        self.data = {}

    def record_order(self, restaurant, total_price):
        if restaurant not in self.data:
            self.data[restaurant] = {'total_orders': 0, 'revenue': 0}
        self.data[restaurant]['total_orders'] += 1
        self.data[restaurant]['revenue'] += total_price

    def get_analytics(self, restaurant):
        return self.data.get(restaurant, 'No data available')

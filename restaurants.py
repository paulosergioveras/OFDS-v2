# Restaurant Profile Management
from reviews import Reviews

class Restaurant():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.menu = {}
        self.reviews = []

    def add_menu_item(self, item, price):
        self.menu[item] = price

    def remove_menu_item(self, item, price):
        if item in self.menu:
            del self.menu[item]
    
    def update_item_price(self, item, new_price):
        if item in self.menu:
            self.menu[item] = new_price
    

    def add_review(self, review):
        self.reviews.append(review)

    def display_reviews(self):
        print("Restaurant Reviews:")
        for review in self.reviews:
            review.show_review()


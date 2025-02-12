# Customer Reviews and Ratings

class Reviews():
    def __init__(self, customer, restaurant, rating, comment):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        self.comment = comment

    
    def show_review(self):
        print(f"Customer: {self.customer}")
        print(f"Restaurant: {self.restaurant.name}")
        print(f"Rating: {self.rating}")
        print(f"Comment: {self.comment}")
        print("-----------------------------")
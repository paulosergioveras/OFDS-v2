# Customer Reviews and Ratings

class Reviews():
    def __init__(self, customer, restaurant, rating, comment):
        self.customer = customer
        self.restaurant = restaurant
        self.set_rating(rating)
        self.comment = comment
    
    def set_rating(self, rating):
        if 0 <= rating <= 5:
            self.rating = rating
        else:
            raise ValueError("Rating must be between 0 and 5")

    def show_review(self):
        print(f'Customer: {self.customer}')
        print(f'Restaurant: {self.restaurant.name}')
        print(f'Rating: {self.rating}')
        print(f'Comment: {self.comment}')
        print('-----------------------------')

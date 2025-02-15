class Promotion():
    def __init__(self):
        self.promotions = {}

    def create_promotion(self, code, discount):
        self.promotions[code] = discount

    def aply_discount(self, code, total_price):
        if code in self.promotions:
            discount = self.promotions[code]
            return total_price * (1 - discount / 100)
        return total_price

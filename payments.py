class Payment():
    def __init__(self):
        self.payment_methods = ['credit_card', 'debit_card', 'money', 'pix']

    def process_payment(self, order, payment_method, payment_detail):
        if payment_method not in self.payment_methods:
            return 'Invalid payment method'

        if payment_method in ['credit_card', 'debit_card']:
            if self.validation_cards(payment_detail):
                return 'Approved: card payment processed successfully'
            else:
                return 'Refused: invalid card'

        elif payment_method == 'pix':
            return 'Payment approved'

        elif payment_method == 'money':
            return 'Payment approved'

    def validation_cards(self, card_detail):
        return isinstance(card_detail.get('card_number'), str) and len(card_detail.get('card_number')) == 16

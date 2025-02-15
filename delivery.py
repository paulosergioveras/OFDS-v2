class DeliveryTracking():
    def __init__(self, order):
        self.order = order
        self.status = 'Preparing'

    def update_status(self, new_status):
        self.stauts = new_status

    def get_status(self):
        return self.status


class DeliveryOptions():
    def __init__(self, delivery_time, instructions):
        self.delivery_time = delivery_time
        self.instructions = instructions

    def update_delivery_time(self, new_delivery_time):
        self.delivery_time = new_delivery_time

    def update_instructions(self, new_instructions):
        self.instructions = new_instructions

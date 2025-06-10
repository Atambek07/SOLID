
from models import Order

class OrderCalculator:
    def calculate_total(self, order: Order) -> float:
        return sum(item.price * item.quantity for item in order.items)

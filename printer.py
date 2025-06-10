
from abc import ABC, abstractmethod
from models import Order

class ReceiptPrinter(ABC):
    @abstractmethod
    def print(self, order: Order):
        pass

class ConsoleReceiptPrinter(ReceiptPrinter):
    def print(self, order: Order):
        print("=== Receipt ===")
        for item in order.items:
            print(f"{item.name} x{item.quantity} = {item.price * item.quantity:.2f}")

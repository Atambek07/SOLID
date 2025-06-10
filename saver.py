
from abc import ABC, abstractmethod
from models import Order

class OrderSaver(ABC):
    @abstractmethod
    def save(self, order: Order):
        pass

class FileOrderSaver(OrderSaver):
    def save(self, order: Order):
        with open("order.txt", "w") as f:
            for item in order.items:
                f.write(f"{item.name},{item.price},{item.quantity}\n")

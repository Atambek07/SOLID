class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

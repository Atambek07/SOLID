
from models import Item, Order
from calculator import OrderCalculator
from printer import ConsoleReceiptPrinter
from saver import FileOrderSaver
from service import OrderService

if __name__ == "__main__":
    order = Order()
    order.add_item(Item("Pizza", 10.99, 2))
    order.add_item(Item("Cola", 2.50, 3))

    calculator = OrderCalculator()
    printer = ConsoleReceiptPrinter()
    saver = FileOrderSaver()

    service = OrderService(calculator, printer, saver)
    service.process_order(order)

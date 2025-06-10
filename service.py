
from models import Order
from calculator import OrderCalculator
from printer import ReceiptPrinter
from saver import OrderSaver

class OrderService:
    def __init__(self, calculator: OrderCalculator, printer: ReceiptPrinter, saver: OrderSaver):
        self.calculator = calculator
        self.printer = printer
        self.saver = saver

    def process_order(self, order: Order):
        total = self.calculator.calculate_total(order)
        print(f"Total: {total:.2f}")
        self.printer.print(order)
        self.saver.save(order)

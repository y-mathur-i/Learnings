"""Module for single responsibility example
"""
from enum import Enum


class Status(Enum):
    """Enum to contain order of the status
    """
    OPEN = "open"
    PAID = "paid"


class Order:
    """Order class
    """
    status = Status.OPEN
    items = []
    quantities = []
    prices = []

    @classmethod
    def set_status(cls, status):
        """Method to set status
        """
        cls.status = status

    def add_item(self, item, quantity, price) -> None:
        """Method to add item to the order
        """
        self.items.append(item)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self) -> int:
        """Method to get sum of total prices
        """
        return sum(p*q for p, q in zip(self.prices, self.quantities))

    # def pay() # a convoluted function handling all and every type of payment

class PaymentProcessor:
    """Class to process payments
    """
    def pay_credit(self, order: Order, security_code: str) -> bool:
        """Method to process payment via credit mode
        """
        print(f"process the order {security_code}")
        order.set_status(Status.PAID)

    def pay_debit(self, order: Order, security_code: str) -> bool:
        """Method to process payment via debit mode
        """
        print(f"process the order {security_code}")
        order.set_status(Status.PAID)



if __name__ == "__main__":
    payment_processor = PaymentProcessor()
    ### now Open/Close principle -> open for extension and closed for modification    
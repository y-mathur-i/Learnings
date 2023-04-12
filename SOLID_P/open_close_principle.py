"""Module for open close start from the code in open close principle.
    open for extension and close for modification
"""
from enum import Enum
from abc import ABCMeta, abstractmethod, ABC


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


class IPaymentProcessor(ABC):
    """Interface for payment processor class
    """
    @abstractmethod
    def pay(self, order: Order, security_code: str) -> None:
        """Method to be implemented by payment method
        """


class DebitPaymentProcessor(IPaymentProcessor):
    """class to process payment via debit mode
    """
    def pay(self, order: Order, security_code: str) -> None:
        print(f"process the order {security_code}")
        order.set_status(Status.PAID)


class CreditPaymentProcessor(IPaymentProcessor):
    """Method to process payment via credit mode
    """
    def pay(self, order: Order, security_code: str) -> None:
        print(f"process the order {security_code}")
        order.set_status(Status.PAID)


if __name__ == "__main__":
    order = Order()
    order.add_item("Milk", 2, 30)
    payment_processor = DebitPaymentProcessor()
    payment_processor.pay(order, "123")
    
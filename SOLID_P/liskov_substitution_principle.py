"""Module for liskov substitution principle. which states that any
    instance can be substituted for it's sub class instance
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
    def pay(self, order: Order) -> None:
        """Method to be implemented by payment method
        """


class DebitPaymentProcessor(IPaymentProcessor):
    """class to process payment via debit mode

    """
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, order: Order) -> None:
        print(f"process the order {self.security_code}")
        order.set_status(Status.PAID)

class CreditPaymentProcessor(IPaymentProcessor):
    """Method to process payment via credit mode
    """
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, order: Order) -> None:
        print(f"process the order {self.security_code}")
        order.set_status(Status.PAID)

class PaypalPaymentProcessor(IPaymentProcessor):
    """Method to process payments for paypal
        uses email instead of a security code
    """
    def __init__(self, email: str) -> None:
        self.email = email
    
    def pay(self, order: Order) -> None:
        print(f"processed order with account {self.email}")
        order.set_status(Status.PAID)



if __name__ == "__main__":
    order = Order()
    order.add_item("Milk", 2, 30)
    payment_processor = DebitPaymentProcessor("sdlfjlksdfj")
    # by removing the dependency of the code now all the payment processors can be swtiched
    payment_processor.pay(order)
    
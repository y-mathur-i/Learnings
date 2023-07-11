"""Principle that tells about how and where the object should be created
Here the object of sale line item is required for functioning of the sale class and does not really need to be exposed to outside world
"""


from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class ProductDesc:
    price: int
    description: str


@dataclass
class SaleLineItem:
    product: ProductDesc
    quantity: int


@dataclass
class Sale:
    items: list[SaleLineItem] = field(default_factory=list)
    time: datetime = field(default=datetime.utcnow())

    def add_line_item(self, product: ProductDesc, quantity: int) -> None:
        self.items.append(SaleLineItem(product, quantity))


def main() -> None:
    headset = ProductDesc(price=5000, description="headset for music")
    keyboard = ProductDesc(price=78000, description="Keyboard")

    # item_one = SaleLineItem(product=headset, quantity=4)
    # item_two = SaleLineItem(product=keyboard, quantity=3)
    sale = Sale()
    # sale = Sale([item_one, item_two])  # now instead of doing this we can pass the product and quantity and the sale class 
    # should create the sale item
    sale.add_line_item(headset, 3)
    sale.add_line_item(keyboard, 5)
    print(sale)

if __name__=="__main__":
    main()

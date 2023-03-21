"""
Proxy design pattern Similar to decorator
It wraps functionality around object creation
"""

from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):
    """Person interface"""
    @abstractmethod
    def basic_method(self) -> None:
        """Basic method to be implemented by derived classes"""

class Person(IPerson):
    """Class implementing Person interface"""

    def basic_method(self) -> None:
        print("Person method")

class ProxyPerson(IPerson):
    """Proxy class for person class"""
    def __init__(self) -> None:
        self.__person = Person()

    def basic_method(self) -> None:
        print("The proxy functionality")
        self.__person.basic_method()

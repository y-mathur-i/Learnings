### purpose ? At runtime decide the kind of object you wish to create
# example -> create a student or teacher object which in turn is a person
from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):  # practice to start with I for an interface
    """
    Interface class 
    """
    @abstractmethod
    def basic_function(self) -> None:
        """Interface method"""

class Student(IPerson):
    """Student class implementing Person interface"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Basic Student name"

    def basic_function(self) -> None:
        print("This a students method")

class Professor(IPerson):
    """Professor class implementing Person interface"""
    def __init__(self) -> None:
        super().__init__()
        self.name = "Basic professor name"

    def basic_function(self) -> None:
        print("This is a professor class")


class PersonFactory:
    """Factory class to create the person"""
    @staticmethod
    def build(person_type: str):
        """Method to build a person based on input"""
        if person_type == "student":
            return Student()
        if person_type == "professor":
            return Professor()
        raise TypeError("Invalid type of person specified")

if __name__=="__main__":
    choice = input("What type of person would you like to create ?")
    person_factory = PersonFactory()
    person = person_factory.build(choice)
    person.basic_function()

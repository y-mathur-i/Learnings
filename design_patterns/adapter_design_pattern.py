"""Module for adapter design pattern in python based on video : https://www.youtube.com/watch?v=bsyjSW46TDg
The idea is to create a common interface for different classes
I seriously doubt i'll ever have to use it unless i am writing new functionality that has to adapt to 
something already written to maintain the uniformity
"""
from abc import ABCMeta, abstractmethod


class Elf:
    """Elf class
    """
    def nall_niv(self):
        """Calling function for elf
        """
        print("Calling as and elf")

class Dwarf:
    """Dwarf class
    """
    def estver_naraho(self):
        """Calling function for dwarf
        """
        print("Calling as a dwarf")

class Human:
    """Human class
    """
    def ring_mig(self):
        """Calling function for human
        """
        print("calling as a human")

class IAdapter(metaclass=ABCMeta):
    """Base adapter interface
    """
    @abstractmethod
    def call_me(self) -> None:
        """Call function
        """

class ElfAdapter(IAdapter):
    """Elf adapter
    """
    def __init__(self, elf: Elf) -> None:
        self.elf = elf

    def call_me(self) -> None:
        self.elf.nall_niv()

class DwarfAdapter(IAdapter):
    """Dwarf adapter
    """
    def __init__(self, dwarf: Dwarf) -> None:
        self.dwarf = dwarf

    def call_me(self) -> None:
        self.dwarf.estver_naraho()

class HumandAdapter(IAdapter):
    """Human adapter
    """
    def __init__(self, human: Human) -> None:
        self.human = human

    def call_me(self) -> None:
        self.human.ring_mig()


if __name__ == "__main__":
    # here we can store instance of each class and then check the instance of the class
    # and call the apt method for it but that list of if else goes too long
    pass
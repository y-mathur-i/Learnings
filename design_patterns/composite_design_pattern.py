"""A class that holds multiple classes implimenting the same interface as itself.
"""
from abc import ABCMeta, abstractmethod
from typing import List


class IDepartment(metaclass=ABCMeta):
    """Department interface
    """
    @abstractmethod
    def __init__(self, employees) -> None:
        """To be implemented
        """

    @abstractmethod 
    def print_dept(self):
        """To be implemented
        """


class AccountDept(IDepartment):
    """Accounting dept implementing dept interface
    """
    def __init__(self, employees) -> None:
        self.employees = employees

    def print_dept(self):
        print(f"Hey, form accounting with {self.employees} employees")

class DevDept(IDepartment):
    """Development dept implementing dept interface
    """
    def __init__(self, employees) -> None:
        self.employees = employees

    def print_dept(self):
        print(f"Hey, form development {self.employees}")


class ParentDept(IDepartment):
    """Parent dept to other depts
    """
    def __init__(self, employees) -> None:
        self.employees = employees
        self.base_emplyees = employees
        self.sub_dept: List[IDepartment] = []

    def add_dept(self, dept: IDepartment):
        """Method to add a sub department
        """
        self.sub_dept.append(dept)
        self.employees += dept.employees

    def print_dept(self):
        print(f"Hey from Parent deptartment with {self.base_emplyees}")
        for dept in self.sub_dept:
            dept.print_dept()
        print(f"Total employees end up being {self.employees}")


def main():
    """Main method to showcase the use case
    """
    a_dept = AccountDept(150)
    d_dept = DevDept(120)
    p_dept = ParentDept(100)
    p_dept.add_dept(a_dept)
    p_dept.add_dept(d_dept)
    p_dept.print_dept()

if __name__ == "__main__":
    main()

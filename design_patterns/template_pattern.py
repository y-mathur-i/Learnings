"""The idea is to have a sequence of steps. Implemented for each object
"""


class Drink:
    """Base for template whose methods witll be overridden
    """
    def follow_recepie(self) -> None:
        self.boil_water()
        self.add_sugar()
        self.add_tea()

    def boil_water(self) -> None:
        print("Boiling water")

    def add_sugar(self) -> None:
        raise NotImplementedError

    def add_tea(self) -> None:
        raise NotImplementedError


class LemonTea(Drink):
    def add_sugar(self) -> None:
        print("Adding sugar")

    def add_tea(self) -> None:
        print("Adding lemon and tea")

class BlackTea(Drink):
    def add_sugar(self) -> None:
        print("adding sugar")

    def add_tea(self) -> None:
        print("adding tea leaves")

if __name__ == "__main__":
    lemon_tea = LemonTea()
    lemon_tea.follow_recepie()
    black_tea = BlackTea()
    black_tea.follow_recepie()

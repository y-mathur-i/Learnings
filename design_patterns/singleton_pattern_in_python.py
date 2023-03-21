"""Module demonstrating singleton design pattern"""

class SingletonClass:
    """Singleton class .i.e there is only one instance of this class at any time"""
    __INSTANCE = None
    _i = 1

    @staticmethod
    def get_instance():
        """Method to get the instance of the class"""
        if SingletonClass.__INSTANCE is None:
            SingletonClass("First instance", SingletonClass._i)
            SingletonClass._i += 1
        return SingletonClass.__INSTANCE

    def __init__(self, name: str, instance_number: int) -> None:
        if SingletonClass.__INSTANCE is not None:
            return
        self._name = name
        self._instance_no = instance_number
        SingletonClass.__INSTANCE = self

if __name__=="__main__":
    singleton_class = SingletonClass.get_instance()
    print(singleton_class.get_instance())  # the address remains the same
    singleton_class_2 = SingletonClass.get_instance()
    print(singleton_class_2.get_instance())  # the address remains the same .i.e the same instance is returned

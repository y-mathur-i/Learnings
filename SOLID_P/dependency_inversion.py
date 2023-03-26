"""Module with code demonstrating dependency inversion
"""
from abc import ABCMeta, abstractmethod
from typing import Any


class IStorage(metaclass=ABCMeta):
    """Interface for class storage
    """
    @abstractmethod
    def get(self, key: str) -> Any:
        """Method to get item from storage based on the key
        """

class AWSStroage(IStorage):
    """Class implementing storage interface with
        AWS interactions for s3
    """
    def get(self, key: str) -> Any:
        print("Calls to s3 storage with BOTO3 client")

class AzureStorage(IStorage):
    """Class implementing storage interface interacting
        with Azure blob storage
    """
    def get(self, key: str) -> Any:
        print("Calls to blob storage")

class Sample:
    """Sample class using storage class
    """
    def __init__(self, storage: IStorage) -> None:
        self.__storage = storage

    def make_call_to_storage(self, key: str) -> None:
        """This is an example for a fucntion that will call the stroage
        """
        self.__storage.get(key)


if __name__ == "__main__":
    # Here we use explicit passing and calls to instantiate the
    # objects but can use something like injector (python package)
    # to bind IStroage any class/implementation we like
    aws_storage = AWSStroage()
    azure_storage = AzureStorage()
    sample_aws = Sample(storage=aws_storage)
    sample_azure = Sample(storage=azure_storage)
    sample_aws.get("Key")
    sample_azure.get("key")

from abc import ABC, abstractmethod

# Abstract Person class
class Person(ABC):
    def __init__(self, name: str, address: str, email: str, phone: str):
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
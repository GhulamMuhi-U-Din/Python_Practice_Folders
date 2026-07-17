# Import Abstract Base Class tools
from abc import ABC, abstractmethod


# Create Abstract Base Class
class Animal(ABC):

    # Every child class
    # must implement this
    @abstractmethod
    def sound(self):
        pass


# Child class
class Dog(Animal):

    # Implement required method
    def sound(self):

        print("Woof")


# Child class
class Cat(Animal):

    # Implement required method
    def sound(self):

        print("Meow")


# Create objects
spike = Dog()

tom = Cat()


# Call methods
spike.sound()

tom.sound()
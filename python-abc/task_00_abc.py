#!/usr/bin/python3

from abc import ABC, abstractmethod


# Definition of the abstract class Animal
class Animal(ABC):
    # Declaration of the abstract method sound
    @abstractmethod
    def sound(self):
        # The abstract method does not have a body/implementation here
        pass


# Definition of the Dog class that inherits from Animal
class Dog(Animal):
    # Implementation of the sound method
    def sound(self):
        return "Bark"


# Definition of the Cat class that inherits from Animal
class Cat(Animal):
    # Implementation of the sound method
    def sound(self):
        return "Meow"

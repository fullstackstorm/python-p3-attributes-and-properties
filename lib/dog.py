#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name = "Fido", breed ="Mastiff"):
        self.set_name(name)
        self.set_breed(breed)

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        # Define a name property for your Dog class. The name must be of type str and between 1 and 25 characters.
        #If the name is invalid, the setter method should print() "Name must be string between 1 and 25 characters."
        if not isinstance(value, str) or len(value) <= 0 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    def get_breed(self):
        return self._breed
    
    def set_breed(self, value):
        if value not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)
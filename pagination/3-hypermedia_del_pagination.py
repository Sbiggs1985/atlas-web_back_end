#!/usr/bin/env python3

class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes here
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        # Print an introduction message
        print(f"Hi, my name is {self.name}, and I am {self.age} years old.")

    def birthday(self):
        # Increment the age and print a birthday message
        self.age += 1
        print(f"Happy Birthday! {self.name} is now {self.age} years old.")

# Create an object of the Person class and test the methods

# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# create a class
from typing import overload


class User:
    # constructor
    def __init__(self, name, age=40):
        self.name = name
        self.age = age

    def say(self):
        return f"{self.name}, {self.age}"

    def has_birthday(self):
        self.age += 1


# extend class
class Customer(User):
    def __init__(self, name, age=40):
        self.name = name
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance += balance

    def say(self):
        return f"{self.name}, {self.age} = {self.balance}"


# init an object
user = User("Gabriel")
user.say()

# properties are accessible
user.has_birthday()
print(user.say())
janet = Customer("Janet", 44)
janet.set_balance(200)
print(janet.say())

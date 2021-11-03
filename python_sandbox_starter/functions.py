from functools import partial

# A function is a block of code which only runs when it is called. In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces

# create a function
def sayHello(name="Rob"):
    print(f"Hello {name}")


sayHello("John Doe")
sayHello()

# return values
def getSum(num1, num2):
    total = num1 + num2
    return total


num = getSum(2, 4)
print(f"{num}")


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression. Very similar to JS arrow functions
getSum = lambda num1, num2: num1 + num2

print(getSum(10, 10))

# decorators - accept function and return a function extended with more bahaviour
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


# apply decorator
@uppercase_decorator
def getURL():
    return "/page/1"


print(getURL())
# partial functions - allow for code reuse
addToTen = partial(getSum, num2=10)
print(addToTen(3))

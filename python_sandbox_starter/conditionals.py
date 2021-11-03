# If/ Else conditions are used to decide to do something based on something being true or false
x = 10
y = 10
# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

if x > y:
    print(f"{x} is greater than {y}")

if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is not greater than {x}")

if x > y:
    print(f"{x} is greater than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{y} is greater than {x}")

# nested
if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{y} is not greater than {x}")
    if x == y:
        print(f"{y} is equal {x}")

# Logical operators (and, or, not) - Used to combine conditional statements

if x > 2 and x <= 10:
    print(f"y:{y}, x:{x}")

if x > 2 or x <= 10:
    print(f"y:{y}, x:{x}")

if not (x == 1):
    print(f"y:{y}, x:{x}")

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object
numbers = [1, 2, 3, 4]
if x in numbers:
    print(f"{x} is in {numbers}")
elif x not in numbers:
    print(f"{x} is not in {numbers}")


# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x is y:
    print(f"{x} is {y}")
# ternanry operator - replacement as of pythin 2.5
x = x if x in numbers else y + 1
# or by indexing a tuple
# x = (falseValue, trueValue)[test that retunrs bool]
x = (y + 1, x)[x in numbers]
x = (y + 1, x)[bool(x in numbers)]

print(f"x is {x}")

# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Gab'
age = 37

#concatenate

print('Hello, my name is ' + name + ' and I am ' + str(age) + ' old') # we can only concatenate strings

# String Formatting - better way to do this
print('My name is {name} and I am {age}'.format(name=name,age=age))

#F-Strings 3.6+ - better
print(f'Hello, my name is {name} and I am {age}')

# String Methods
s = 'Helllo World'

#Capitalize
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
print(s.replace('World','Friends'))
print(s.count('ll'))
print(s.startswith('he'))
print(s.endswith('d'))
print(s.split()) #splits into a list - default separator is space?
print(s.find('l')) #finds position of str 
print(s.isalpha())
print(s.isnumeric())
print(s.istitle())
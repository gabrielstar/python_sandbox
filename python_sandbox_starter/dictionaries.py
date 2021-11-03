# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# it is indexed
person = {"first_name": "John", "last_name": "Doe"}
# use constructor
person2 = dict(first_name="Sarah", last_name="Williams")

# get value
print(person.get("first_name"))
print(person["first_name"])  # more common

# add key value
person["phone"] = "111-222-333"

# get dict keys
print(person.keys())
print(person.items())

# copy a dictionary
person2 = person.copy()  # similar to spread operator in JS
person2["city"] = "Wrocław"

# remove
del person2["city"]
person2.pop("last_name")

# clear
person.clear()
# del person

# getlength
print(len(person2))


print(person, type(person))
print(person2, type(person2))

# list of dict
people = [{"name": "Gabriel", "age": 20}, {"name": "Tom", "age": 22}]
print(people)
# refer to item
print(people[1]["name"])

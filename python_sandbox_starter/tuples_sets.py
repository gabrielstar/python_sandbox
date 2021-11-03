# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# unchangable is important here

fruits = ("apples", "oranges")
fruits2 = tuple(("Apples", "Oranges"))
fruits2 = "Apples"  # wo trailing comma it is string
fruits2 = ("Appples",)  # single value tuple
# fruits[2] = 'Kiwi' - cannot be done, tuples are immutable

# delet tuple
del fruits

print(len(fruits2))
print(fruits2)
print(fruits2, type(fruits2))

# A Set is a collection which is unordered and unindexed. No duplicate members.
fruits_set = {"Apples", "Apples"}
print(f"Set: {fruits_set}")

# check in set
print("Apples" in fruits_set)
# add to set
fruits_set.add("Grape")
fruits_set.add("Apples")  # adding same thing does have no effect
fruits_set.remove("Grape")
fruits_set.clear()  # clears set content
# del fruits_set # deletes object

print(fruits_set)

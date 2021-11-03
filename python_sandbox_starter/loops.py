# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["Tom", "Rom", "Bom"]

for person in people:
    print(f"name: {person}")

# break
for person in people:
    if person == "Rom":
        # break
        continue  # skips
    print(f"name: {person}")

for i in range(len(people)):
    print(people[i])

for i in range(0, 10, 2):
    print(i)

# While loops execute a set of statements as long as a condition is true.

count = 0
while count <= 10:
    print(f"Count {count}")
    count += 1

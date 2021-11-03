# Python has functions for creating, reading, updating, and deleting files.

# create
myFile = open("myfile.txt", "w")

# print
print("Name " + myFile.name)
print("Closed? " + str(myFile.closed))
print("Mode " + myFile.mode)

# write
myFile.write("I love python")
myFile.close()

# append
with open(
    "myfile.txt", "a"
) as file:  # with acquires a resouce - https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for
    file.writelines("I like JS")
# resource is automatically closed when we leave the scope

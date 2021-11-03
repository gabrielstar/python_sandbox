# A List is a collection which is ordered and changeable. Allows duplicate members.

# create a list
numbers = [1,2,3,4]
fruits = ['apples','pears','oranges']
# with construtor - rathert not used too much
numbers2 = list((1,2,3,4))

print(numbers, numbers2)


print(fruits)
#get a value
print(fruits[0])
print(len(fruits))

#append
fruits.append('mangos')
#remove
fruits.remove('mangos')
#insert into position
fruits.insert(0,'grapes')
#remove with pop
print(f'removing {fruits.pop(1)}')
#sort
fruits.sort()
fruits.sort(reverse=True)
#change value
fruits[0] = 'potatoes'

print(fruits)
# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets.

# create set in python
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

my_set = set([1, 2, 3, 4, 5])
print(my_set)
print(type(my_set))

#addding elements
number = {1, 2,  3,  4, 5}
number.add(10)
print(number)

# removing elements
fruits = {'apple', 'mango', 'orange'}
fruits.remove('mango')
print(fruits)

#discard elements
fruits = {'apple', 'mango', 'orange'}
fruits.discard('banana')
print(fruits)


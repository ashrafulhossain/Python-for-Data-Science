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

# union
set1 = {1, 2, 3,}
set2 = {3, 4, 5}
set_union = set1.union(set2)
print(set_union)

#intersection
set_a = {'ashraful', 'rakib', 'shakib', 'nokib'}
set_b = {'rakib', 'jashim', 'ashraful','jakir'}
set_inter = set_a.intersection(set_b)
print(set_inter)

#difference
set1 = {1, 2, 3,}
set2 = {3, 4, 5}
set_dif = set1.difference(set2)
print(set_dif)

#symetric difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7}
set_symetric = set1.symmetric_difference(set2)
print(set_symetric)
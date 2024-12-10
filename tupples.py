# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#access
tup = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tup[2:5])


tup = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tup[:4])

tup = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tup[-5:-2])

tup = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if 'apple' in tup:
    print('yes')
else:
    print('no')

#update tupples

countries = ('spain', 'bangladesh', 'usa', 'nepal', 'germany')
update_tup = list(countries)
update_tup.append('singapur')
countries = tuple(update_tup)
print(countries)



countries = ('spain', 'bangladesh', 'usa', 'nepal', 'germany')
update_tup = list(countries)
update_tup[3] = 'austria'
countries = tuple(update_tup)
print(countries)

countries = ('spain', 'bangladesh', 'usa', 'nepal', 'germany')
update_tup = list(countries)
update_tup.pop(1)
countries = tuple(update_tup)
print(countries)
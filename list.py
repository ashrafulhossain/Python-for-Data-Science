# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets

marks = [3, 5, 6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])


marks = [3, 5, 6, 'Ashraf', True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

# List index
colour = ['red', 'green', 'yellow']
print(colour[0])
print(colour[1])
print(colour[2])

# Negative indexing
marks = [3, 5, 6, 'Ashraf', True]
print(marks[-3])
print(marks[len(marks)-3])

jump = [3, 5, 6, 'Ashraf', True, 6, 7, 2, 32, 345, 23]
print(jump)
print(jump[1:8])
print(jump[1:8:3])


list = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(list[-4:-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
else:
    print('No','apple is  not in the fruits list')


list = ["apple", "banana", "cherry", "mango"]
list[2] = 'orange'
print(list)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


list = ["apple", "banana", "cherry", "mango"]
list.insert(1, 'orange')
print(list)


list = ["apple", "banana", "cherry", "mango"]
list.append('watermilon')
print(list)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


list = ["apple", "banana", "cherry"]
add_list = ("kiwi", "orange")
list.extend(add_list)
print(list)
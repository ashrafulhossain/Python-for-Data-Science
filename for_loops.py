# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


name = 'Ashraful'
for i in name:
    print(i)
    if (i == 'r'):
     print('somethig very special')

colours = ['Red', 'Green', 'Blue', 'Black', 'Yellow']
for colour in colours:
    print(colour)
    if colour == 'Black':
        print('My favourite colour')
    for i in colour:
        print(i)


person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in person.items():
    print(f"{key}: {value}")

colours = {
    'red' : 'rose',
    'black' : 'shirt',
    'blue' : 'sky',
    'yellow' : 'orrange'
}
for key, value in colours.items():
    print(f"{key}: {value}")
    if key == 'red' and value == 'rose':
        print('its my faboure rose')


numbers = (10, 20, 30, 40)
for number in numbers:
    print(number)


for k in range(10):
    print(k)

for k in range(1, 11):
    print(k)

for k in range(0, 101, 10):
    print(k)

for i in range(0, 11):
    if i % 2 == 0:
        print(f'{i} is even number')
    else:
        print(f'{i} is a odd number')






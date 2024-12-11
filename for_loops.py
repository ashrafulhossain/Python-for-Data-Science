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



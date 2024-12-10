a = 33
b = 200
if b > a:
  print("b is greater than a")

a = 333
b = 333
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")




username = 'ashraful'
password = '123456'
if username == 'ashraful' and password == '123456':
  print('login succesful')
else:
  print('login failed')


age = 20
if age < 30:
  print("Age is less then 30")
  print("Age is getter then equal to 30")


age = 40
if age < 30:
  print('age is less then 30')
elif age > 30 or age < 35:
  print('age is between 30 and 35')
else:
  print('age is greater then or equal 30')
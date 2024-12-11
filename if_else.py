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


score = 78
if score >= 90:
  print("Letter grade is: ", 'A')
elif score >= 80:
  print("Letter grade is ", 'B')
elif score >= 70:
  print("Letter grade is ", 'C')
elif score >= 60:
  print("Letter grade is ", 'D')
else:
  print("Letter grade is " 'F')


score = 80
if score >= 90:
 letter_grade = 'A'
elif score >= 80:
 letter_grade = 'B'
elif score >= 70:
  letter_grade = 'C'
elif score >= 60:
  letter_grade = 'D'
else:
   letter_grade = 'F'



# condition
is_rain = False
is_winter = True

if is_rain :
   print("Take the umbrella as well as raincoat")

elif is_winter :
   print("wear warm clothes")

else:
    print("go out normally")

print("Enjoy  your day")

print("letter grade:", letter_grade)


num = int(input("please enter a number: "))
if num > 0:
  print("you have entered a positve number")
elif num < 0:
  print("you have entered a negative number")
else:
  print("you have entered a zero number")
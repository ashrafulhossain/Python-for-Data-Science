# Python divides the operators in the following groups:
# Arithmetic operators : +, -, *, /, %, **, //.
# Assignment Operators : =, +=, -=, *=, /=, %=, //=, >>=, <<=.
# Comparison Operators : ==, !=, >, < , >=, <=.
# Logical Operators : and, or, not.
# Identity Operators : is, is not.
# Membership Operators : in, not in

# Arithmetic operators
a = 10
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# Assignment Operators

a = 20
print(a)

a += 5 # a = a + 5
print(a)

a -= 3 # a = a - 5
print(a)

a *= 5 # a= a * 5
print(a)

# Logical Operators
x = 10
# And operators
res = x > 5 and x < 20
print(res)

#Or operators
res1 = x < 5 or x > 8
print(res1)

#Not operators
res2 = not(x < 5 and x < 20)
print(res2)


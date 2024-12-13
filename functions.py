# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# In Python a function is defined using the def keyword.

# Features of Functions:
 # > Code Reusability: Once written, a function can be used multiple times.
 # > Organized Code: Large programs can be divided into smaller, manageable parts.
 # > Easy Debugging: Errors can be identified more easily.
 # > Parameter Passing: Data can be passed into the function for processing.


def calculate(a, b):
    total = a + b
    return total
sum = calculate(10, 20)
print(sum)



def calculate(a, b):
    total = a + b
    substraction = a - b
    return total, substraction

sum = calculate(20, 10)
print(sum)


def calculate(a, b):
    total = a + b
    substraction = a - b
    multipication = a * b
    return total, substraction, multipication

sum = calculate(20, 10)
print(sum)

def calculate(a, b):
    total = a + b
    substraction = a - b
    multipication = a * b
    return total, substraction, multipication

sum = calculate(20, 10)
print(sum)


def calculate(a, b):
    total = a + b
    substraction = a - b
    multipication = a * b
    division = a / b
    return total, substraction, multipication, division

sum = calculate(20, 10)
print(sum)


def isGreater(x, y):
    if x > y:
        return 'X is greater than Y'
    else:
        return 'X is less than Y'

character = isGreater(50, 40)
print(character)


def is_prime(num):

    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

number = 29
print(f"Is {number} prime? {is_prime(number)}")

def reverse_string(s):
    return s[::-1]
text = "Python"
print("Reversed string:", reverse_string(text))



def factorial(n):

    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
number = 5
print(f"Factorial of {number}:", factorial(number))


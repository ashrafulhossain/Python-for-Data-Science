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

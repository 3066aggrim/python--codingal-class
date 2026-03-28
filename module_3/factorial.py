def factorial(number):
    ''' this is a recursive function to find a factorial of a number'''

    if number == 1 or number == 0:
        return 1

    else:
        return number*factorial(number-1)


print(factorial.__doc__)
print("the factorialof 0:", factorial(0))
print("the factorialof 1:", factorial(1))
print("the factorialof 2:", factorial(2))
print("the factorialof 3:", factorial(3))
print("the factorialof 4:", factorial(4))
print("the factorialof 5:", factorial(5))

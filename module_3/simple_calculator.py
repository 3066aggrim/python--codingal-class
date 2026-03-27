def add(P, Q):
    return P+Q


def subtract(P, Q):
    return P-Q


def multiplication(P, Q):
    return P*Q


def division(P, Q):
    return P/Q


print("please select an operaton")
print("a=Add")
print("b=Sub")
print("c=multiplication")
print("d=Division")

choice = input("a,b,c,d")

num1 = int(input("please enter a number"))
num2 = int(input("plese select another number"))

if choice == "a":
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == "b":
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == "c":
    print(num1, "*", num2, "=", multiplication(num1, num2))

elif choice == "d":
    print(num1, "/", num2, "=", division(num1, num2))

else:
    print("invalid input")

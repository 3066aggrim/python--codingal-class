try:
    num = int(input("please enter a number: "))
    print("hello")
except ValueError as num:
    print(num)
print("valueError")

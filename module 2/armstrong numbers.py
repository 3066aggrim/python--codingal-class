number = int(input("please enter a 3 digit number"))
sum = 0
temp = number

while temp > 0:
    digit = temp % 10
    sum += digit**3
    temp //= 10

if number == sum:
    print("it is an armstrong number")

else:
    print("it is not an armstrong number")

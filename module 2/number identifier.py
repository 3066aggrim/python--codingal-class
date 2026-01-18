number = int(input("please enter a  any digit number"))
count = 0


while number > 0:
    count = count+1
    number //= 10

print("count=", count)

num = int(input("please enter any digit number"))
t = num
numlen = 0

while t > 0:
    numlen = numlen+1
    t = int(t/10)


if numlen >= 4:
    numlen = int(numlen/2)
    check = 0

    while num > 0:
        rem = num % 10
        if check == numlen:
            midone = rem

        elif check == (numlen-1):
            midtwo = rem

        num = int(num/10)
        check = check+1

product = midone*midtwo

print("\n The produt of the mid digits are",
      midone, midtwo, "their product is", product)

valid = False

while not valid:
    try:
        n = int(input("enter  number"))
        while n % 2 == 0:
            print("bye")
            valid = True
            break

    except ValueError:
        print("invalid input")

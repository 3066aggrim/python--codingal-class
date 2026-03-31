

while True:
    try:
        age = (int(input("please enter your age: ")))
        print("valid output")

        if age % 2 == 0:
            print("your age is even")
            break

        elif age % 2 != 0:
            print("your age is odd")
            break

    except ValueError:
        print("its a value error")

    finally:
        print("Completed")

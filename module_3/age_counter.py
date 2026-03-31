age = (int(input("please enter your age: ")))

while True:
    try:
        print("valid output")

        if age % 2 == 0:
            print("your age is even")
            break

        elif age % 2 != 0:
            print("your age is odd")
            break

    except ValueError:
        print("its a value error")

    except ZeroDivisionError:
        print("Zero Division Error")

    finally:
        print("Completed")

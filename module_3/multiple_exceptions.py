try:
    num1 = int(input("please enter your number: "))
    num2 = int(input("please enter a number:"))
    result = num1/num2
    print("your answer is: ", result)
    print("your result wasnt:", result1)

except ValueError:
    print("value error")

except NameError:
    print("NameError")

except ZeroDivisionError:
    print("Zero division error")

except SyntaxError:
    print("syntax error")

finally:
    print("hello i will be printed no matter what")

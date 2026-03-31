import random

number = str(random.randint(10, 12))

print("I will select a number and you have to guess it ")
print("If you guess it correctly you will win")


while True:
    guess = int(input("please enter a number: "))

    if number == guess:
        print("You have done it!🎉🎉🎉")

        break

    else:
        print("Try again")

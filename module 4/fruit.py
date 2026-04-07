numbers = int(input("please enter a range of numbers"))
user_value = int(input("Enter a number: "))

odd_numbers = []

for num in numbers:
    if num % 2 != 0 and num < user_value:
        odd_numbers.append(num)

print("Odd numbers below input:", odd_numbers)

# Now Fruits

fruits = ["apple", "banana", "mango", "orange", "grapes"]

New_fruits = []
